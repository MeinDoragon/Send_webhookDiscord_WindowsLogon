import requests

#Webhook of my channel. Click on edit channel --> Webhooks --> Creates webhook
mUrl = "<Webhook link here>"

data = {"content": 'HELLO EVERYONE'}
response = requests.post(mUrl, json=data)

print(response.status_code)

print(response.content)