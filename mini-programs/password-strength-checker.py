import string

def check_password_validity():

    while True:

        password = input("Password: ").strip()
        has_invalid_char = False

        for char in password:

            if char in string.punctuation or char == ' ':
                has_invalid_char = True
            
        if has_invalid_char:
            print("You cannor use punctuation or spaces!")
            continue

        if len(password) > 0:

            return password
        
        else:
            print("Please write a password!")


def password_checker(password):

    score = 0

    if len(password) >= 8:
        score += 1

    has_digit = False
    has_upper = False
    has_lower = False

    for char in password:

        if char.isdigit():
            has_digit = True
        
        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True
     
    score += has_lower + has_upper + has_digit

    if score == 1:

        return "Weak"
    
    elif score == 2:

        return "Decent"
    
    elif score == 3:

        return "Strong"
    
    elif score == 4:

        return "Very Strong"


password = check_password_validity()
strength = password_checker(password)

print("Your password is ", strength)