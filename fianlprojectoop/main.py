class book():
    def __init__(self, title, author, release_year):
        self.title = title
        self.author = author
        self.release_year = release_year
class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_all_books(self):
        for book in self.books:
            print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
