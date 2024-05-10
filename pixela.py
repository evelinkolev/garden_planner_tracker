import requests


class Pixela:

    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.graph_id = "graph1"
        self.header = {
            "X-USER-TOKEN": self.token
        }

    def create_new_user(self):
        user_param = {
            "username": self.username,
            "token": self.token,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }

        response = requests.post(url=self.pixela_endpoint, json=user_param)

        print(response.text)
        print(f"https://pixe.la/@{self.username}")

    def delete_user(self):
        url = f"{self.pixela_endpoint}/{self.username}"

        response = requests.delete(url=url, headers=self.header)
        print(response.text)
