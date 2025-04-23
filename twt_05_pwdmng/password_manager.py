import base64
import os

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def get_path(filename) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    return file_path


def load_key():
    key = ""
    try:
        with open(get_path("key.key"), "rb") as file:
            key = file.read()
    except FileNotFoundError:
        with open(get_path("key.key"), "wb") as key_file:
            key_file.write(Fernet.generate_key())
        return load_key()

    return key


def get_fernet(password) -> Fernet:
    salt = load_key()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    return Fernet(key)


def view(fer: Fernet):
    try:
        with open(get_path("passwords.txt"), "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, pwd = data.split("|")
                try:
                    print(f"User: {user} | Password: {fer.decrypt(pwd.encode()).decode()}")
                except InvalidToken:
                    # print(f"Cannot decode a password with provided key for user: {user}")
                    continue
    except FileNotFoundError:
        print("File with passwords not found. First, add a new password")


def add(fer: Fernet):
    user = input("Account Name: ")
    pwd = fer.encrypt(input("Password: ").encode())

    with open(get_path("passwords.txt"), "a") as f:
        f.write(user + "|" + pwd.decode() + "\n")


def password_manager():
    master_pwd = input("What is the master password? ").encode()
    fer = get_fernet(master_pwd)

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
