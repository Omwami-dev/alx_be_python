class Book:
    def __init__(self, title , author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"'{self.title}' by {self.author}"
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {super().__str__()} [Page Count: {self.page_count}]"


class Library:
    """Class to manage a collection of books."""

    def __init__(self):
        self.books = []  # A list to store books

    def add_book(self, book: Book):
        """Adds a book to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Book added: {book}")
        else:
            raise ValueError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        """Lists all books in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        