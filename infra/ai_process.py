import os
import json

# Klasörleri oluştur
os.makedirs("backend/src/routes", exist_ok=True)

# Dosya yolları
input_file = "data/events_raw.json"
output_file = "backend/src/routes/events_processed.json"

# Mock AI işleme
with open(input_file, "r") as f:
    events = json.load(f)

# Her etkinliği kategorilendirip özet ekleyelim
for event in events:
    event["category"] = "Music / Art"  # Mock kategori
    event["summary"] = f"{event['name']} etkinliği {event['location']}’da {event['date']} tarihinde gerçekleşiyor."
    event["recommendation"] = "Mutlaka gidin!"  # Mock öneri

# İşlenmiş veriyi kaydet
with open(output_file, "w") as f:
    json.dump(events, f, indent=4)

print(f"AI processed data saved at {output_file}")
