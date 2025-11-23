import os
import openai

# GitHub Secrets'tan API key al
openai.api_key = os.getenv("OPENAI_API_KEY")

# AI prompt ve kod üretme
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # GPT-4 yerine GPT-3.5 kullanıyoruz
    messages=[
        {"role": "system", "content": "You are a senior Node.js developer."},
        {"role": "user", "content": "Implement a backend route for 'events' that fetches events data."}
    ],
    temperature=0.3
)

# AI'dan gelen kodu al
code = response.choices[0].message.content

# Dosyaya yaz
output_file = "backend/src/routes/events.js"
with open(output_file, "w") as f:
    f.write(code)

print(f"AI code generated at {output_file}")
