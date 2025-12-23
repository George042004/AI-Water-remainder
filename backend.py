import time
import json
import os
from plyer import notification

DATA_FILE = "hydration_data.json"

print("🚀 Tracker started! Checking for dehydration every 10 seconds...")

while True:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                drunk = data.get("water_drunk", 0)
                weight = data.get("weight", 75)
                
                # Goal: 35ml per kg
                goal = int(weight * 35)
                
                # DEHYDRATION LOGIC:
                # If you have drunk less than 50% of your goal, you are "Dehydrated"
                if drunk < (goal * 0.5):
                    status_title = "⚠️ STATUS: DEHYDRATED"
                    message_text = f"Warning! You only had {drunk}ml. You need {goal - drunk}ml more!"
                else:
                    status_title = "✅ STATUS: HYDRATED"
                    message_text = f"Great job! Total: {drunk}ml. You are meeting your goal!"

                notification.notify(
                    title=status_title,
                    message=message_text,
                    timeout=5
                )
            except Exception as e:
                print(f"Error reading file: {e}")
    
    # Check every 10 seconds for testing
    time.sleep(10)
