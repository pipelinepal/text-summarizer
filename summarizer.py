import requests

with open("key.txt") as f:
    key = f.read().strip()

with open("article.txt", "r") as f:

    text = f.read()

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"

headers = {"x-goog-api-key": key, "Content-Type": "application/json"}

body = {"contents":[{"parts": [{"text": "summarize this text in 3 lines:"+ text}]}]}


response = requests.post(url, headers=headers, json=body, timeout=60)

print(response.status_code)

data = response.json()



summary = data["candidates"][0]["content"]["parts"][0]["text"]

print(summary)

with open("summary.txt", "w") as f:
    f.write(summary)
