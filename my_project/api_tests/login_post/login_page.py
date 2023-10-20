import requests

# post.login
class LoginPage:
    def __init__(self):
        self.base_url = "https://reqres.in"
        self.session = requests.Session()

    def login(self, email, password):
        data = {
            "email": email,
            "password": password
        }
        response = self.session.post(f"{self.base_url}/api/login", json=data)
        return response
    def cleanup(self):
        self.session.close()