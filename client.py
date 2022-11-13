import requests

url = "http://127.0.0.1:8001/sentiment-analysis"

headers = {'Content-type': 'application/x-www-form-urlencoded'}
texts = {"text": "Shinka Network builds self-optimising & self-governing networks for diverse agents to co-evolve. Each agent focuses on their fields of expertise and leaves the rest for network collaboration."}
# texts = {"text": "i hate you"}

r = requests.post(url, data=texts , headers=headers)


print(r.json())