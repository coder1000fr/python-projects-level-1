import random
import string

def generate_password(min_length, numbers=True, special_charactors=True):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    charactors = letters
    if numbers:
        charactors += digits
    if special_charactors:
        charactors += punctuation

    pwd = ''
    has_numbers = False
    has_special = False
    meets_criteria = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(charactors)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in punctuation:
            has_special = True


        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_charactors:
            meets_criteria = meets_criteria and has_special


    return pwd

min_length = int(input('Enter minimum password length: '))
has_numbers = input('Do you want to have numbers? (y/n): ').lower() == 'y'
has_specials = input('Do you want to have special charactors? (y/n): ') == 'y'

print(f'Your password is:  {generate_password(min_length, has_numbers, has_specials)}')
