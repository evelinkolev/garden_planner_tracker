import requests
from datetime import datetime


def get_today():
    today = datetime.today()
    return today.strftime('%Y%m%d')


class Pixela:

    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.graph_id = "garden1"
        self.today = get_today()
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

    def create_graph(self, graph_name, graph_unit="Seeds", graph_type="int", graph_color="kuro"):

        url = f"{self.pixela_endpoint}/{self.username}/graphs"

        body = {
            "id": self.graph_id,
            "name": graph_name,
            "unit": graph_unit,
            "type": graph_type,
            "color": graph_color,
        }

        response = requests.post(url=url, json=body, headers=self.header)
        print(response.text)
        print(f"{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}.html")

    def delete_graph(self):
        url = f"{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}"
        response = requests.delete(url=url, headers=self.header)
        print(response.text)

    def post_pixel(self, quantity, date=None):
        if date is None:
            date = self.today

        url = f"{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}"

        body = {
            "date": date,
            "quantity": quantity,
        }

        response = requests.post(url=url, headers=self.header, json=body)
        print(response.text)
