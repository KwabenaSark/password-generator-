import random

def generate_password(length: int) -> str:
    password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""

    for i in range(length):
        password += random.choice(password_chars)

    return password

print(generate_password(8))
