import requests
import json
 
with open('user_data.json','r') as json_File :
    sample_load_file=json.load(json_File)
    user_phone_number = sample_load_file.get("user_mobile_number", "")
    api = sample_load_file.get("api", "")
    message = sample_load_file.get("message", "")

url = "https://fiotext.com/send-sms"
form_data = {"user_api_key": api,
             "sms_message": message,
             "sms_to_phone": user_phone_number}
server = requests.post(url, data=form_data)
output = server.text

print(output)