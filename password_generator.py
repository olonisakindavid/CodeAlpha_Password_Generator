# Password Generator
import random
import string


def generate_password(minimum_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False
    contains_number = False
    contains_special = False

    while not meets_criteria or len(password) < minimum_length:
        new_character = random.choice(characters)
        password += new_character

        if new_character in digits:
            contains_number = True
        elif new_character in special:
            contains_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = contains_number
        if special_characters:
            meets_criteria = meets_criteria and contains_special
    return password


min_length = int(input("Enter the minimum Length: "))
contains_number = input("Do you want to have numbers? (y/n?) ").lower() == "y"
contains_special = input(
    "Do you want to have any special characters? (y/n)").lower() == "y"
password = generate_password(min_length, contains_number, contains_special)
print("The generated password is:", password)
