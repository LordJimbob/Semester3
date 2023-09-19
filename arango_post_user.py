import requests
query = {"query": "FOR user IN users RETURN user"}
r = requests.post("http://127.0.0.1:8529/_api/cursor", json=query, auth=("root", "kjm42asr"))
print(r.text)
