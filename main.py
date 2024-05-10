from pixela import Pixela

PIXELA_USER = "testov"  # Validation rule: [a-z][a-z0-9-]{1,32}
PIXELA_TOKEN = "IwanttoT3s7this047"  # Validation rule: {8,128}characters

try_account = Pixela(username=PIXELA_USER, token=PIXELA_TOKEN)
#try_account.create_new_user()  # Run this only once
#try_account.delete_user()  # DANGER!

#try_account.create_graph("Graph") # https://pixe.la/v1/users/testov/graphs/graph1.html
#try_account.delete_graph(graph_code="graph1")


