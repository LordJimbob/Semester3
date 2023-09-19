import yaml
with open('data.yaml', 'r', encoding="utf-8") as file:
    prime_service = yaml.safe_load(file)
print(f"Hi {prime_service['name']} {prime_service['last_name']}")
for sibling in prime_service["siblings"]:
    print(sibling.get("name"))