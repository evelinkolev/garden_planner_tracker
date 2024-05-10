import requests


class Pixela:

    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.graph_id = None
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
        self.graph_id = graph_name.strip().lower() + "1"

        #print(f"Graph Name:{graph_name} / GraphId: {self.graph_id}")

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

    def delete_graph(self, graph_code=None):
        if graph_code is None:
            graph_code = self.graph_id

        url = f"{self.pixela_endpoint}/{self.username}/graphs/{graph_code}"
        response = requests.delete(url=url, headers=self.header)
        print(response.text)
