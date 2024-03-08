class Book:
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
            print('title: ', book.title, '\nauthor: ', book.author, '\nrelease year: ', book.release_year)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print('title: ', book.title, '\nauthor: ', book.author, '\nrelease year: ', book.release_year)
                return
        return
def main():
    book_manager = BookManager()
    while True:
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Search for a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter publication year: ")
            new_book = Book(title, author, year)
            book_manager.add_book(new_book)
            print("Book added successfully!")

        elif choice == "2":
            print("\n--- All Books ---")
            book_manager.display_all_books()
            print("-----------------")

        elif choice == "3":
            title = input("Enter the title of the book you want to search for: ")
            found_book = book_manager.search_book(title)
            if found_book:
                print("Book found:")
                print(found_book)
            else:
                print("Book not found.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
