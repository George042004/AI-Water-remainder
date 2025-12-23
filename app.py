import streamlit as st
import json
import os
from datetime import datetime

# The filename must match your background tracker
DATA_FILE = "hydration_data.json"

st.set_page_config(page_title="Hydration Tracker", page_icon="💧")
st.title("💧 Hydration Tracker")

# --- DATA LOADING LOGIC ---
def load_data():
    today = datetime.now().strftime("%Y-%m-%d")
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                # If the file is from a previous day, reset to 0
                if data.get("date") != today:
                    return {"water_drunk": 0, "weight": 75, "date": today}
                return data
            except:
                # If file is corrupted, return defaults
                return {"water_drunk": 0, "weight": 75, "date": today}
    # If file doesn't exist, start fresh
    return {"water_drunk": 0, "weight": 75, "date": today}

data = load_data()

# --- SIDEBAR / SETTINGS ---
st.sidebar.header("Settings")
weight = st.sidebar.number_input("Your Weight (kg)", value=int(data["weight"]), min_value=1)
daily_goal = int(weight * 35)

# --- MAIN INTERFACE ---
st.metric("Total Water Drunk Today", f"{data['water_drunk']} ml")
st.write(f"Your daily goal based on weight: **{daily_goal} ml**")

# Progress bar calculation
progress = min(data['water_drunk'] / daily_goal, 1.0)
st.progress(progress)

# Input for adding water
add_water = st.number_input("Add water intake (ml)", value=250, step=50)

if st.button("Log Water"):
    # CUMULATIVE LOGIC: New amount + Old total
    data["water_drunk"] += add_water
    data["weight"] = weight
    data["date"] = datetime.now().strftime("%Y-%m-%d")
    
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
    
    st.success(f"Added {add_water}ml! Total is now {data['water_drunk']}ml.")
    st.rerun()

# Emergency Reset
if st.sidebar.button("Reset Daily Progress"):
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    st.rerun()
