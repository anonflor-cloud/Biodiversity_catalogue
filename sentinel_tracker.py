import csv
import datetime
import os

# 📅 Date
today = datetime.date.today()
print("🌿 Eco Sentinel Tracker 🛰️")
print(f"📅 Date: {today}")

# 🌧️ Rainfall
try:
    rainfall = float(input("🌧️ How much rain fell today (in mm)? "))
    if rainfall < 5:
        condition = "Dry"
    elif rainfall < 20:
        condition = "Normal"
    else:
        condition = "Wet"
except ValueError:
    print("⚠️ Invalid input. Setting rainfall to 0 mm and condition to 'Dry'.")
    rainfall = 0
    condition = "Dry"

# 🌱 Plant
plant_name = input("🌱 Plant Name (Latin or Common): ")
plant_location = input("📍 Enter plant location code or description: ")

# 🦌 Wildlife
wildlife_seen = input("🦌 Wildlife seen today? (e.g. '3 caprioli'): ")
wildlife_notes = input("📝 Wildlife notes (optional): ")

# 🧾 Save
filename = "eco_sentinel_log.csv"
entry = [today, rainfall, condition, plant_name, plant_location, wildlife_seen, wildlife_notes]

file_exists = os.path.isfile(filename)
with open(filename, mode="a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["Date", "Rainfall (mm)", "Condition", "Plant", "Location", "Wildlife Seen", "Wildlife Notes"])
    writer.writerow(entry)

print("\n✅ Data logged successfully. Frank would be proud.")
print(f"📄 Entry: {entry}")

