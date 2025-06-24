class Book:
    def __init__(self, data):
        self.isbn = data.get("isbn")
        self.title = data.get("title")
        self.author = data.get("author")
        self.publisher = data.get("publisher")
        self.pages = data.get("pages")

    def is_valid(self):
        return all([self.isbn, self.title, self.author])
