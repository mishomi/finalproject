import json
class Book:
    def __init__(self, title, author, release_year):
        self.title = title
        self.author = author
        self.release_year = release_year

class BookManager:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self): #used to load every book from bookdata.json onto our list books to be used in the following functions
        try:
            with open('bookdata.json', 'r') as f:
                self.books = json.load(f)
        except FileNotFoundError: # in case there is an error and we cant find our json file
            self.books = []

    def save_books(self): # load every book back onto our json file
        with open('bookdata.json', 'w') as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, book): # we check if we have a book with  given author, name and date in our books list
        for existing_book in self.books:
            if (existing_book['title'] == book.title and existing_book['author'] == book.author and existing_book['release_year'] == book.release_year):
                return False
        self.books.append({'title': book.title, 'author': book.author, 'release_year': book.release_year})
        self.save_books()
        return True

    def display_all_books(self):
        for book in self.books:
            print('\ntitle: ', book['title'], '\nauthor: ', book['author'], '\nrelease year: ', book['release_year'])

    def search_book(self, title):# by checking using lower() function, we make sure our search is not case sensitive
        found_books = []
        for book in self.books:
            if title.lower() in book['title'].lower():
                found_books.append(book)
        return found_books

def main():
    book_manager = BookManager()
    while True:
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Search for a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1": # we add the book if it is not already on the list, as previously mentioned
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            while True:
                year = input("Enter publication year: ")
                if year.isdigit():#check if we were given proper date
                    year = int(year)
                    break
                else:
                    print("Please enter a valid year (as a number).")
            new_book = Book(title, author, year)
            if book_manager.add_book(new_book): #check if book is already on our list
                print("Book added successfully!")
            else:
                print("Book already in the database")
        elif choice == "2":
            print("\n--- All Books ---")
            book_manager.display_all_books()
            print("-----------------")
        elif choice == "3":
            title = input("Enter the title of the book you want to search for: ")
            found_books = book_manager.search_book(title)
            if found_books:
                print("Books found:")
                for book in found_books:
                    print('title: ', book['title'], '\nauthor: ', book['author'], '\nrelease year: ', book['release_year'])
                print("------------------")
            else:
                print("Book not found.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
