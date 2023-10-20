import requests

class APIClient:
    def __init__(self, base_url, path, headers, json_data):
        self.base_url = base_url
        self.path = path
        self.headers = headers
        self.json_data = json_data

    def post_data(self):
        url = f"{self.base_url}{self.path}"
        response = requests.post(url, headers=self.headers, json=self.json_data)
        return response