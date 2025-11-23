import os
import json

# Klasör oluştur
os.makedirs("data", exist_ok=True)

# Mock veri (gerçek scraper sonrası değişecek)
events = [
    {"id": 1, "name": "Concert in Park", "date": "2025-11-25", "location": "Istanbul"},
    {"id": 2, "name": "Art Exhibition", "date": "2025-11-27", "location": "Ankara"}
]

# JSON dosyasına kaydet
with open("data/events_raw.json", "w") as f:
    json.dump(events, f, indent=4)

print("Scraper mock data saved at data/events_raw.json")
