import random
import string

def generate_password(length):
    lc= string.ascii_lowercase  
    uc = string.ascii_uppercase  
    d= string.digits              
    sc = string.punctuation  

    all_characters = lc + uc + d + sc

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6 characters): "))
            if length < 6:
                print("Password length should be at least 6 characters. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    new_pwd = generate_password(length)
    print("Generated Password:", new_pwd)

if __name__ == "__main__":
    main()
