import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_PATH = os.path.join(BASE_DIR, 'names.txt')

def main():

    try:

        members = load_members()

        if members:

            print('Current members: \n')

            for member in members:

                print(member.title())

        while True:

            print('Options:')

            print('1. Add Name')
            print('2. Quit')

            choice = input()

            if choice == '1':

                add_name(members)

            elif choice == '2':

                save_and_quit(members)
                sys.exit()

    except (EOFError, KeyboardInterrupt):
        print("Bye!")
        sys.exit()

def add_name(members):

    name = input("What's you name? ")
    members.append(name + '\n')

def save_and_quit(members):

    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

    with open(FILE_PATH, 'w') as file:
        file.writelines(members)

        print()

    for member in members:
        print(member.lower().title(), end='')
        print('-' * 10)

def load_members():

    try:

        with open(FILE_PATH, 'r') as file:
            return file.readlines()

    except FileNotFoundError:

        return []

if __name__ == '__main__':
    main()
