# Library Management System - My Own Logic

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Issued"
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)

class Library:
    def __init__(self):
        self.books = []

    def search_book(self, book_id):
        # Changed Logic: using while + index, not for loop
        index = 0
        while index < len(self.books):
            if self.books[index].book_id == book_id:
                return self.books[index]
            index = index + 1
        return None

    def add_book(self, book):
        if self.search_book(book.book_id) is not None:
            print("Error: Book ID already exists!")
        else:
            self.books.append(book)
            print("Book added successfully!")

    def view_books(self):
        if self.books == []:
            print("Library is empty. No books to show.")
            return

        print("\n========== BOOK LIST ==========")
        # Changed Logic: while loop for viewing also
        i = 0
        while i < len(self.books):
            print()
            self.books[i].display()
            print("-------------------------------")
            i = i + 1

    def issue_book(self, book_id):
        book = self.search_book(book_id)
        # Changed Logic: nested if, not elif
        if book is None:
            print("Error: Book not found!")
        else:
            if book.is_available:
                book.is_available = False
                print("Book issued successfully!")
            else:
                print("Sorry! This book is already issued.")

    def return_book(self, book_id):
        book = self.search_book(book_id)
        if book is None:
            print("Error: Book not found!")
        else:
            if book.is_available:
                print("This book is already in library.")
            else:
                book.is_available = True
                print("Book returned successfully!")

def main():
    library = Library()
    running = True

    while running:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            id_text = input("Enter Book ID: ")
            # Changed Logic: isdigit() instead of try/except
            if not id_text.isdigit():
                print("Please enter numbers only for ID.")
                continue
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            book = Book(int(id_text), title, author)
            library.add_book(book)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            id_text = input("Enter Book ID: ")
            if not id_text.isdigit():
                print("Please enter numbers only.")
                continue
            book = library.search_book(int(id_text))
            if book is None:
                print("Error: Book not found!")
            else:
                print("\nBook Found!\n")
                book.display()

        elif choice == "4":
            id_text = input("Enter Book ID: ")
            if id_text.isdigit():
                library.issue_book(int(id_text))
            else:
                print("Please enter numbers only.")

        elif choice == "5":
            id_text = input("Enter Book ID: ")
            if id_text.isdigit():
                library.return_book(int(id_text))
            else:
                print("Please enter numbers only.")

        elif choice == "6":
            print("Thank you! Bye Bye...")
            running = False

        else:
            print("Wrong choice! Choose 1 to 6 only.")

main()