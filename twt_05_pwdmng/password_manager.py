from cryptography.fernet import Fernet

def write_key():
    with open("key.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())

def load_key():
    key = ""
    try:
        with open("key.key", "rb") as file:
            key = file.read()
    except FileNotFoundError:
        write_key()
        return load_key()

    return key


def view(fer: Fernet):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print(f"User: {user} | Password: {fer.decrypt(pwd.encode()).decode()}")

def add(fer: Fernet):
    user = input("Account Name: ")
    pwd = fer.encrypt(input("Password: ").encode())

    with open("passwords.txt", "a") as f:
        f.write(user + "|" + pwd.decode() + "\n")

def password_manager():
    master_pwd = input("What is the master password? ")
    key = load_key() + master_pwd.encode()
    fer = Fernet(key)

    while True:
        mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
        if mode == 'q':
            break
        
        if mode == "view":
            view(fer)
        elif mode == "add":
            add(fer)
        else:
            print("Invalid mode.")
            continue

password_manager()
