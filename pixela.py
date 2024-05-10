import requests


class Pixela:

    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.pixela_endpoint = "https://pixe.la/v1/users"
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

        if response.status_code == 200:
            return True
