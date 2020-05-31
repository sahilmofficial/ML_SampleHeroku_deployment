import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':1.5})

print(r.json())