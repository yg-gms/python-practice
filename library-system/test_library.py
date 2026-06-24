from library import add_books, add_members, borrow_book, return_books

def test_add():

    library = {
        "books": {

            "JDUE34": {'title': 'harry potter', 'author': 'rowling', 'available': True}
            
        },
        "names": {}
    }

    assert add_books(library, 'John', 'Cat', 'JS9323') == True
    assert add_books(library, 'rowling', 'harry potter', 'JDUE34') == False
