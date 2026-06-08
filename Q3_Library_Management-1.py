# Library Management System

books = []

def add_book():
    book = input("Enter book name: ")
    books.append(book)
    print("Book added successfully.")

def search_book():
    book = input("Enter book name to search: ")
    if book in books:
        print("Book found.")
    else:
        print("Book not found.")

def remove_book():
    book = input("Enter book name to remove: ")
    if book in books:
        books.remove(book)
        print("Book removed successfully.")
    else:
        print("Book not found.")

def display_books():
    if books:
        print("\nAvailable Books:")
        for b in books:
            print("-", b)
    else:
        print("No books available.")

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        remove_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")
