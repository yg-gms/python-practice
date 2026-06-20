import random

def give_hint(guess, secret_number):

    if guess < secret_number:
        return "Too low!"
    elif guess > secret_number:
        return "Too large!"
    else:
        return "WOW! Correct!"
    
def get_valid_difficulty():
    
    while True:
        try: 
            difficulty = input("What is your difficulty? (easy/medium/hard/random) ").lower()
            match difficulty:

                case "easy" | "medium" | "hard" | "random":
                    return difficulty
                
                case _:
                    print("Please choose a correct difficulty!")
            
        except ValueError:
            print("Invalid Input! Please enter correct difficulty!")

def get_valid_guess():
    
    while True:
        try:
            guess = int(input("What's your guess? "))
            if 1 <= guess <= 100:
                return guess
            
        except ValueError:
            print("Invalid Input! Please enter a correct value!")

def guessing_game():

    difficulty = get_valid_difficulty()

    if difficulty == "easy":
        max_number = 50
        max_attempts = 10
    elif difficulty == "medium":
        max_number = 100
        max_attempts = 7
    elif difficulty == "hard":
        max_number = 200
        max_attempts = 6
    elif difficulty == "random":
        max_number = random.randint(50, 200)
        max_attempts = random.randint(5, 15)

    secret = random.randint(1, max_number)
    attempts = 0

    print(f"Guess the number between 1 and {max_number}!")
    print(f"You have {max_attempts} attempts!")

    while attempts < max_attempts:
        guess = get_valid_guess()
        attempts += 1

        result = give_hint(guess, secret)
        print(result)

        if guess == secret:
            print("Congrats, you win!")
            return

    print(f"You lose! The number was {secret}")

guessing_game()

