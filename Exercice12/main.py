class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    # méthodes
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                self.books.remove(book)
                break

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                self.borrow_books.append(book)
                break

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title.lower() == book_title.lower():
                self.borrow_books.remove(book)
                self.books.append(book)
                break

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books(self):
        return [book.title for book in self.borrow_books]
