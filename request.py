import requests

url = 'http://localhost:5000/predict_api' 
r = requests.post(url,json={'drivenKM':300,'model':0})

print(r.json())

