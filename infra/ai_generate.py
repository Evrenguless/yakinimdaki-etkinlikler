import os
import openai
from pathlib import Path

# OpenAI API key: GitHub Secrets -> OPENAI_API_KEY
# Doğru
openai.api_key = os.getenv("OPENAI_API_KEY")

# Örnek prompt: backend için route oluştur
prompt = """
Implement an Express route GET /api/events/nearby?lat=&lng=&radius= 
that queries Postgres (table events with lat,lng cols) using ST_DWithin if PostGIS exists, 
otherwise use Haversine. Return JSON { events: [...] } limited to 50.
Provide full JS file content.
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a senior Node.js developer."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3
)

# AI çıktısını dosyaya yaz
output_dir = Path("../backend/src/routes")
output_dir.mkdir(parents=True, exist_ok=True)
file_path = output_dir / "events.js"

code = response['choices'][0]['message']['content']
with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

print(f"AI code generated at {file_path}")
