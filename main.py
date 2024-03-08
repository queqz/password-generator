import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Type the lenght of digits for the password: "))
            if length <= 0:
                print("The length must be over 0, please use a higher number.")
                continue
            break
        except ValueError:
            print("Hm, this didn't work. Please type in a other number.")
    
    generated_password = generate_password(length)
    print("Your generated password:", generated_password)

if __name__ == "__main__":
    main()
