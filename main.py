from pixela import Pixela

PIXELA_USER = "evelin"  # Validation rule: [a-z][a-z0-9-]{1,32}
PIXELA_TOKEN = "fdFDDGXCVBFbbfs3421sd"  # Validation rule: {8,128}characters

try_account = Pixela(username=PIXELA_USER, token=PIXELA_TOKEN)
try_account.create_new_user()  # Run this only once


