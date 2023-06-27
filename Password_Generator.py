# Robert Gleason
# Version 1
# Password Generator
import random
import string


def options():
    print("Please select an option")
    print("1. Generate a password")
    print("2. Quit")
    user_in = input()
    return user_in


def length_input():
    print("What is the minimum length you would like your password to have?")
    passwd_length = int(input())
    return passwd_length


def numbers_input():
    print("Would you like your password to have numbers in it?")
    nums_input = input()
    has_nums = False
    if nums_input == "Yes" or nums_input == "yes":
        has_nums = True
    return has_nums


def special_input():
    print("Would you like your password to have special characters in it?")
    has_specials = False
    special_input = input()
    if special_input == "Yes" or special_input == "yes":
        has_specials = True
    return has_specials


def generate_password(min_length, numbers, special_char):
    """ Creates and returns a random password based on the parameters passed """
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    selection = letters
    pwd = ""

    if numbers:
        selection += digits
    if special_char:
        selection += special_characters

    while len(pwd) < min_length:
        # chooses a random character from
        new_character = random.choice(selection)
        pwd += new_character

    print(len(pwd))
    return pwd


if __name__ == '__main__':
    print("Welcome to the password generator.")
    while True:
        user_in = options()
        if user_in == "1":
            length = length_input()
            # checks if length is greater than 8
            while length < 8:
                print(f'The length you entered, {length}, is not long enough to make a secure password.'
                      f' Please enter a valid length.')
                length = length_input()
            # gets the values from the user and call generate_password method
            nums = numbers_input()
            special = special_input()
            password = generate_password(length, nums, special)
            print(f'Your password with the length of {length} characters is {password}')
        elif user_in == "2":
            print("Shutting Down, Goodbye")
            break
        else:
            print("I'm sorry, that option does not exist, please try again.")
