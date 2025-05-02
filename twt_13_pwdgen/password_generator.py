import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # check out meets criteria
        meets_criteria = True
        if len(pwd) < min_length:
            meets_criteria = False        
        else:
            if numbers:
                meets_criteria = has_number
            if special_characters:
                meets_criteria = meets_criteria and has_special

    return pwd


def main():
    min_length = int(input("Enter minimum length of the password: "))
    has_number = input("Should the password contains numbers (Y/n)? ").lower() != "n"
    has_special = input("Should the password contains special characters (Y/n)? ").lower() != "n"
    pwd = generate_password(min_length, has_number, has_special)
    print(f"The generated password is: {pwd}")

if __name__ == "__main__":
    main()