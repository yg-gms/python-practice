def main():

    width = int(input("Enter the width of the shape: "))
    height = int(input("Enter the height of the shape: "))

    print("Choose shape from below: ")
    print("1. Rectangle")
    print("2. Triangle")

    choice = int(input())

    if choice == 1:
        rectangle(width, height)

    elif choice == 2:
        triangle(height)
    
def rectangle(width, height):
    for i in range(height):
        print('*' * width)

def triangle(height):
    for i in range(1, height + 1):
        print('*' * i)


if __name__ == "__main__":
    main()