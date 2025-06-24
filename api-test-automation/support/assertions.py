

def assert_book_count(user, expected_count):
    actual = len(user.books)
    assert actual == expected_count, f"Esperado {expected_count} livros, mas encontrou {actual}"

def assert_user_has_isbns(user, expected_isbns):
    user_isbns = [book.isbn for book in user.books]
    missing = set(expected_isbns) - set(user_isbns)
    assert not missing, f"O(s) ISBN(s) {missing} não foram encontrados nos livros do usuário"
