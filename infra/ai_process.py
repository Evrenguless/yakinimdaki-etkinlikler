import os
import json
import requests

# Dosya yolları
input_file = "data/events_raw.json"
output_file = "backend/src/routes/events_processed.json"

# Mock AI işleme (şimdilik gerçek API çağrısı yok, test için)
with open(input_file, "r") as f:
    events = json.load(f)

# Her etkinliği kategorilendirip özet ekleyelim
for event in events:
    event["category"] = "Music / Art"  # Mock kategori
    event["summary"] = f"{event['name']} etkinliği {event['location']}’da {event['date']} tarihinde gerçekleşiyor."
    event["recommendation"] = "Mutlaka gidin!"  # Mock öneri

# Klasörleri oluştur
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# İşlenmiş veriyi kaydet
with open(output_file, "w") as f:
    json.dump(events, f, indent=4)

print(f"AI processed data saved at {output_file}")
