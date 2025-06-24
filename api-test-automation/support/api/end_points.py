import requests
from support.api.base_request import BaseRequest

class EndPoints(BaseRequest):
    def create_user(self, username, password):
        payload = {
            "userName": username,
            "password": password
        }
        return self.post("/Account/v1/User", json=payload)

    def generate_token(self, username, password):
        payload = {
            "userName": username,
            "password": password
        }
        return self.post("/Account/v1/GenerateToken", json=payload)

    def authorize_user(self, username, password):
        payload = {
            "userName": username,
            "password": password
        }
        return self.post("/Account/v1/Authorized", json=payload)

    def get_books(self):
        return self.get("/BookStore/v1/Books")

    def get_user_details(self, user_id, token):
        headers = {"Authorization": f"Bearer {token}"}
        return self.get(f"/Account/v1/User/{user_id}", headers=headers)

    def delete_user(self, user_id, token):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        url = f"{self.base_url}/Account/v1/User/{user_id}"
        response = requests.delete(url, headers=headers)
        
        return response