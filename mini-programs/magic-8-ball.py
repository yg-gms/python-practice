import random

def magicball():

    responses = [
        "For sure!", "Yes, definitely", "Maybe not...", 
        "Without a doubt!", "Absolutely!", "Mhm", "Cannot tell you that...",
        "My sources say no", "Most likely"
    ]

    print("Welcome to the Magic 8-Ball!")
    print("Please ask me a yes/no question!")

    question_number = 0

    while True:

        question = input("Ask me anything: ").lower()
         
        if question == "quit":
            print("Alright, bye!")
            break

        if question.endswith("?"):
            print(random.choice(responses))
        
        else:
            print("Please ask a question ending with a question mark!")

        question_number += 1

        if question_number == 5:
            print("You asked 5 questions, wow!")
        
        if question_number == 10:
            print("You asked 10 questions, you're very curious!")

magicball()