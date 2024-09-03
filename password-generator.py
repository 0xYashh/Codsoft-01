import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    if length > 0:
        password = generate_password(length)
        print("Your Generated Password:", password)
    else:
        print("Password length must be greater than 0.")

main()
