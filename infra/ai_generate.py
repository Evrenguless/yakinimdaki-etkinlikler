import os
import requests
import json

# GitHub Secrets'tan API key al
API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://api.openrouter.ai/v1/chat/completions"

if not API_KEY:
    raise ValueError("OpenRouter API key is missing. Add it as a secret named OPENROUTER_API_KEY.")

# Mesajları oluştur
messages = [
    {"role": "system", "content": "You are a senior Node.js developer."},
    {"role": "user", "content": "Implement a backend route for 'events' that fetches nearby events and returns JSON data."}
]

# API çağrısı
headers = {"Authorization": f"Bearer {API_KEY}"}
data = {
    "model": "llama-2-7b-chat",
    "messages": messages,
    "temperature": 0.3
}

response = requests.post(API_URL, headers=headers, json=data)
result = response.json()

# AI'dan gelen kodu al
code = result["choices"][0]["message"]["content"]

# Dosyaya yaz
output_file = "backend/src/routes/events.js"
with open(output_file, "w") as f:
    f.write(code)

print(f"AI code generated at {output_file}")
