import time
import json
import os
from plyer import notification

DATA_FILE = "hydration_data.json"

print("🚀 Background hydration tracker running...")

while True:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        drunk = data.get("water_drunk", 0)
        weight = data.get("weight", 75)
        goal = int(weight * 35)

        if drunk < goal * 0.5:
            notification.notify(
                title="🚨 Dehydration Alert",
                message=f"You drank only {drunk}ml. Drink water now!",
                timeout=5
            )
        elif drunk < goal * 0.8:
            notification.notify(
                title="⚠️ Hydration Reminder",
                message="You are getting dehydrated.",
                timeout=5
            )

    time.sleep(600)  # every 10 minutes
