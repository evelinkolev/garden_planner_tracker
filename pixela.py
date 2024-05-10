class Pixela:

    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.header = {
            "X-USER-TOKEN": self.token
        }

