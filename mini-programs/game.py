import sys
import random

def main():

    max_number = 100
    max_guesses = 10

    print("Welcome to the guessing game!")
    print(f"You have {max_guesses} amount of guesses in order to find a number between 1 and {max_number}!")

    number = random.randint(1, max_number)
    attempts = 0

    while attempts < max_guesses:

        try:

            if attempts == max_guesses:
                print("You lose!")
                return

            guess = int(input("Number: "))
            attempts += 1

            win = hint(guess, number, max_guesses, attempts)

            if win:
                return
            else:
                continue


        except ValueError, EOFError, KeyboardInterrupt:
            if ValueError:
                print("Invalid input")
            else:
                sys.exit()
            continue

    print(f"You lose! The number was {number}")

def hint(guess, number, max_guesses, attempts):

    if guess < number:
        print(f"Too Low! Attempts left: {max_guesses - attempts}")

    elif guess > number:
        print(f"Too Large! Attempts left: {max_guesses - attempts}")
                
    elif guess == number:
        print(f"Congrats, you win in {attempts} tries!")
        return True


        
    

if __name__ == "__main__":
    main()