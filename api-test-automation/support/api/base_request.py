import requests

class BaseRequest:
    def __init__(self):
        self.base_url = "https://demoqa.com"
        self.headers = {
            "Content-Type": "application/json"
        }

    def get(self, endpoint, headers=None, **kwargs):
        all_headers = self.headers.copy() if self.headers else {}
        if headers:
            all_headers.update(headers)
        return requests.get(f"{self.base_url}{endpoint}", headers=all_headers, **kwargs)

    def post(self, endpoint, json=None, **kwargs):
        return requests.post(f"{self.base_url}{endpoint}", headers=self.headers, json=json, **kwargs)

    def rent_books(self, user_id, isbns, token):
        headers = self.headers.copy()
        headers["Authorization"] = f"Bearer {token}"
        payload = {
            "userId": user_id,
            "collectionOfIsbns": [{"isbn": i} for i in isbns]
        }
        return requests.post(f"{self.base_url}/BookStore/v1/Books", json=payload, headers=headers)


    def associate_book_to_user(self, user_id, isbn, token):
        headers = self.headers.copy()
        headers["Authorization"] = f"Bearer {token}"
        payload = {
            "userId": user_id,
            "isbn": isbn
        }
        response = requests.put(
            f"{self.base_url}/BookStore/v1/Books/{isbn}",
            json=payload,
            headers=headers
        )
 
        return response