import csv
import os

class Book:
    def __init__(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status  # Available or Issued

    def to_list(self):
        return [self.title, self.author, self.isbn, self.status]

    @staticmethod
    def from_list(data):
        return Book(data[0], data[1], data[2], data[3])

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self.status}")

class LibraryManager:
    def __init__(self, filename="books.csv"):
        self.filename = filename

    def load_books(self):
        books = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    books.append(Book.from_list(row))
        return books

    def save_books(self, books):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "ISBN", "Status"])
            for book in books:
                writer.writerow(book.to_list())

    def add_book(self, book):
        books = self.load_books()
        books.append(book)
        self.save_books(books)
        print("Book added successfully.")

    def display_books(self):
        books = self.load_books()
        if not books:
            print("No books found.")
        for book in books:
            book.display()

    def search_book(self, keyword):
        books = self.load_books()
        found = False
        for book in books:
            if keyword.lower() in book.title.lower() or keyword == book.isbn:
                book.display()
                found = True
        if not found:
            print("Book not found.")

    def issue_book(self, isbn):
        books = self.load_books()
        for book in books:
            if book.isbn == isbn:
                if book.status == "Available":
                    book.status = "Issued"
                    self.save_books(books)
                    print("Book issued successfully.")
                    return
                else:
                    print("Book is already issued.")
                    return
        print("Book not found.")

    def return_book(self, isbn):
        books = self.load_books()
        for book in books:
            if book.isbn == isbn:
                if book.status == "Issued":
                    book.status = "Available"
                    self.save_books(books)
                    print("Book returned successfully.")
                    return
                else:
                    print("Book is already available.")
                    return
        print("Book not found.")

# ==============================
# User Menu
# ==============================

def main():
    manager = LibraryManager()

    while True:
        print("\n--- Library Book Tracker ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            manager.add_book(book)

        elif choice == '2':
            manager.display_books()

        elif choice == '3':
            keyword = input("Enter Title or ISBN to search: ")
            manager.search_book(keyword)

        elif choice == '4':
            isbn = input("Enter ISBN to issue: ")
            manager.issue_book(isbn)

        elif choice == '5':
            isbn = input("Enter ISBN to return: ")
            manager.return_book(isbn)

        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
