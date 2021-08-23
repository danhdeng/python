import json
import requests
import pyttsx3


response = requests.get(("https://fakerapi.it/api/v1/companies?_quantity=5"))
print(response.text)
jsonData = json.loads(response.text)
print(jsonData["data"][0]["name"])

pyttsx3.speak(jsonData["data"][0]["name"])


