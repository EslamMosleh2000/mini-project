class Book:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability

    def check_out(self):
        if self.availability:
            self.availability = False
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"Sorry, '{self.title}' is already checked out.")

    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"'{self.title}' has been returned and is now available.")
        else:
            print(f"'{self.title}' was not checked out.")

    def display_info(self):
        status = "Available" if self.availability else "Checked out"
        print(
            f"Title: {self.title}\nAuthor: {self.author}\nStatus: {status}\n")


class LibraryCatalogue:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' by {book.author} has been added to the catalogue.")

    def display_all_books(self):
        if not self.books:
            print("No books in the catalogue.")
        else:
            for book in self.books:
                book.display_info()


def main():
    catalogue = LibraryCatalogue()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", False)

    catalogue.add_book(book1)
    catalogue.add_book(book2)
    catalogue.add_book(book3)

    print("\nLibrary Catalogue:")
    catalogue.display_all_books()

    print("\nChecking out 'The Great Gatsby':")
    book1.check_out()

    print("\nAttempting to check out 'To Kill a Mockingbird':")
    book3.check_out()

    print("\nReturning 'The Great Gatsby':")
    book1.return_book()

    print("\nUpdated Library Catalogue:")
    catalogue.display_all_books()

    print("\nAdding a new book to the catalogue:")
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    new_book = Book(title, author)
    catalogue.add_book(new_book)

    print("\nFinal Library Catalogue:")
    catalogue.display_all_books()


if __name__ == "__main__":
    main()
