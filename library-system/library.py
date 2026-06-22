def create_library():
    return {
        "books": {},
        "names": {},
    }

def add_books(library, author, title, isbn):

    if isbn in library['books']:
        print("Book already exists!")
        return False
    
    library["books"][isbn] = {

        "title": title,
        "author": author,
        "available": True
    }

    print(f"Added: {title}")
    return True

def add_members(library, member_id, name):

    if member_id in library['names']:
        print("Member already exists!")
        return
    
    library["names"][member_id] = {

        "name": name,
        "borrowed": []

    }
    print(f"New member: {name}")

def borrow_book(library, member_id, isbn):

    if member_id not in library["names"]:
        print("This member doesn't exist!")
        return False
    
    member = library["names"][member_id]
    
    if isbn not in library["books"]:
        print("This book doesn't exist!")
        return False
    
    book = library["books"][isbn]
    
    if not book["available"]:
        print("Book is unavailable!")
        return False
    
    if len(member["borrowed"]) >= 3:
        print("Too many books borrowed!")
        return False

    book["available"] = False
    member["borrowed"].append(isbn)
    print(f"{book['title']} borrowed succesfully!")
    return True

def display_books(library):

    if not library["books"]:
        print("No books to display :(")
        return
    
    print("-" * 40)
    
    for isbn, book in library['books'].items():
        status = "Available" if book["available"] else "Borrowed"
        print(f"{(book['title']).upper()}")
        print(f"   Author: {book['author']}")
        print(f"   Status: {status}")
        print("-" * 40)

def display_members(library):

    if not library["names"]:
        print('No members of library :(')
        return
    
    for member_id, member in library["names"].items():
        print(f"{member['name'].upper()}")
        print(f"  ID: {member_id}")
        print(f"  Books borrowed: {len(member['borrowed'])}")
        print("-" * 40)



my_library = create_library()

def main():

    while True:
        print("Welcome to the library! Choose one of the options to continue!")

        print("1. Display Books")
        print("2. Display Members")
        print("3. Add Books")
        print("4. Add Members")
        print("5. Borrow Book")

        while True:

            try:

                choice = input()

                if choice == '1':
                    display_books(my_library)
                    break

                elif choice == '2':
                    display_members(my_library)
                    break

                elif choice == '3':
                    add_books(my_library, input("Author: "), input("Title: "), input("ISBN: "))
                    break

                elif choice == '4':
                    add_members(my_library, input("Member ID: "), input("Name: "))
                    break

                elif choice == '5':
                    borrow_book(my_library, input("Member ID "), input("ISBN: "))
                    break

                else:
                    print("Please enter a valid choice!")
                    break

            except (EOFError, KeyboardInterrupt):
                print("Bye!")
                break

if __name__ == "__main__":
    main()