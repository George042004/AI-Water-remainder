import streamlit as st
import json
import os
from datetime import datetime

DATA_FILE = "hydration_data.json"

st.set_page_config(page_title="Hydration Tracker", page_icon="💧")
st.title("💧 Hydration Tracker")

def load_data():
    today = datetime.now().strftime("%Y-%m-%d")
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            if data.get("date") != today:
                return {"water_drunk": 0, "weight": 75, "date": today}
            return data
    return {"water_drunk": 0, "weight": 75, "date": today}

data = load_data()

st.sidebar.header("Settings")
weight = st.sidebar.number_input("Your Weight (kg)", value=int(data["weight"]))
daily_goal = int(weight * 35)

st.metric("Total Water Drunk Today", f"{data['water_drunk']} ml")
st.write(f"Daily Goal: **{daily_goal} ml**")

st.progress(min(data['water_drunk'] / daily_goal, 1.0))

add_water = st.number_input("Add water (ml)", 250, step=50)

if st.button("Log Water"):
    data["water_drunk"] += add_water
    data["weight"] = weight
    data["date"] = datetime.now().strftime("%Y-%m-%d")
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
    st.success("Water logged!")
    st.rerun()
