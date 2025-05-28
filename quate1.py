class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

class BookPrinter:
    @staticmethod
    def print_info(book: Book):
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Content: {book.content}")

class BookEditor:
    @staticmethod
    def update_content(book: Book, new_content: str):
        book.content = new_content

class BookSaver:
    @staticmethod
    def save_to_file(book: Book, filename: str):
        with open(filename, 'w') as f:
            f.write(f"{book.title}\n{book.author}\n{book.content}")

if __name__ == "__main__":
    book = Book("1984", "George Orwell", "Big Brother is watching you.")
    BookPrinter.print_info(book)

    BookEditor.update_content(book, "War is peace. Freedom is slavery.")
    BookPrinter.print_info(book)

    BookSaver.save_to_file(book, "book.txt")
