import requests

class APIClient:
    def __init__(self, base_url, path, headers):
        self.base_url = base_url
        self.path = path
        self.headers = headers

    def get_data(self):
        url = f"{self.base_url}{self.path}"
        response = requests.get(url, headers=self.headers)
        return response