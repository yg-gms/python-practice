import sys
from cryptography.fernet import Fernet

'''
def get_key():

    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key


def main():

    try:

        key = load_key()
        fer = Fernet(key)

        # 2 options: See passwords list, add a password

        print("Welcome to your password manager. Please pick an option:")

        print("1. View Passwords")
        print("2. Add a Password")
        print("Q to Quit")

        # loop the process, user can add/view passwords until quit

        while True:

            mode = input("Choice (1 or 2): ").lower().strip()

            # exit system (quit) if q is entered (case insensitive)

            if mode == 'q':
                sys.exit()

            # call viewing or adding function based on input

            if mode == '1':
                view(fer)

            elif mode == '2':
                add(fer)

            else:
                print("Please enter a valid choice!")
                continue

    except EOFError:
        sys.exit("Bye!")

def view(fer):
        
        try:

            # open file in read mode and print contents as lines in a for loop
            with open('passwords.txt', 'r') as file:

                for line in file.readlines():
                    data = line.rstrip()

                    user, passw = data.split('|')
                    print(f"{user}: {fer.decrypt(passw.encode()).decode()}")

        # if there is a FileNotFoundError, notify user and handle the error

        except FileNotFoundError:
            print("You don't have any passowrds!")

def add(fer):

    # ask user for username and passowrd, append it to passwords.txt
    
    username = input("Account Username: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as file:
        file.write(f"{username}|{fer.encrypt(pwd.encode()).decode()}\n")

if __name__ == "__main__":
    main()