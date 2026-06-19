user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().title()

if user_input == "42":
    print("Yes")

elif user_input == "Forty Two":
    print("Yes")

elif user_input == "Forty-Two":
    print("Yes")

else:
    print("No")