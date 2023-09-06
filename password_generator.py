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

    password = ""
    meets_criteria = False
    contains_number = False
    contains_special = False

    while not meets_criteria or len(password) < min_length:
        new_character = random.choice(characters)
        password += new_character

        if new_character in digits:
            contains_number = True
        elif new_character in special:
            contains_special = True

        meets_criteria = True


generate_password(10)
