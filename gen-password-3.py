import string
import random

def generate_password(length,
                      use_uppercase=True,
                      use_numbers=True,
                      use_symbols=True):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    all_characters = lower + upper + numbers + symbols

    password = ''.join(random.choice(all_characters)for _ in range(length))

    return password

print(generate_password(12))
