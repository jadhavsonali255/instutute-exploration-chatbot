import requests

response = requests.get('C:/Users/jadha/PycharmProjects/Foundation_Project/chatbot-deployment-main/static/style.css', headers={'Cache-Control': 'no-cache'})

print(response.status_code)
