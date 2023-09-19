import time
import requests

with open("user_data.csv", "a", encoding="utf-8") as my_file:
        number = input("Enter number: ")
        message = input("Enter message: ")
        my_file.write(f"\n{number}¤{message}¤{int(time.time())}")

url = "https://fiotext.com/send-sms"
form_data = {"user_api_key": "3c31d12838e1434072fd927dc3636c71",
             "sms_message": message,
             "sms_to_phone": number}
server = requests.post(url, data=form_data)
print(server.text)