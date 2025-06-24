from support.models.book import Book

class User:
    def __init__(self, json_data):
        self.user_id = json_data.get("userID")
        self.username = json_data.get("username")
        self.books = [Book(b) for b in json_data.get("books", [])]

    def has_books(self, expected_count):
        return len(self.books) == expected_count

    def has_books_with_isbns(self, expected_isbns):
        user_isbns = [book.isbn for book in self.books]
        return set(expected_isbns).issubset(user_isbns)
