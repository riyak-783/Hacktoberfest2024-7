class Library:
    def __init__(self):
        self.books = ["1984", "To Kill a Mockingbird", "The Great Gatsby"]
        self.borrowed_books = []

    def display_books(self):
        print("\nAvailable books:")
        for book in self.books:
            print(book)

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            self.borrowed_books.append(book_name)
            print(f"You borrowed '{book_name}'")
        else:
            print(f"'{book_name}' is not available")

    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            self.books.append(book_name)
            print(f"You returned '{book_name}'")
        else:
            print(f"You don't have '{book_name}' to return")

# Main application
library = Library()

while True:
    print("\nLibrary Menu")
    print("1. Display books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    
    choice = input("Choose an option: ")

    if choice == '1':
        library.display_books()

    elif choice == '2':
        book_name = input("Enter the book name: ")
        library.borrow_book(book_name)

    elif choice == '3':
        book_name = input("Enter the book name to return: ")
        library.return_book(book_name)

    elif choice == '4':
        break

    else:
        print("Invalid choice, try again.")
