import requests
import json
users_keys = ["2298", "2409"]
for key in users_keys:
    res = requests.get(f"http://127.0.0.1:8529/_api/document/users/{key}", auth=("root", "kjm42asr"))
    res = json.loads(res.content)
    print(f" Hi {res.get('name')} {res.get('last_name')}, your age is {res.get('age')}")