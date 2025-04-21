# upgraded_app.py
import streamlit as st
import random
import time
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="AI Data Center Dashboard")

# --- HEADER ---
st.title("🌐 AI-Powered Edge Data Center")
st.caption("Real-time monitoring, intelligent control, and operator interaction")

# --- USER LOGIN SIMULATION ---
st.sidebar.header("🔐 Operator Panel")
user = st.sidebar.text_input("Username", "admin")
password = st.sidebar.text_input("Password", type="password")
if user != "admin" or password != "admin123":
    st.sidebar.warning("Please login with valid credentials.")
    st.stop()
else:
    st.sidebar.success("Access granted ✅")

# --- SIMULATED SERVER RACK DATA ---
def generate_data():
    racks = ["Rack A", "Rack B", "Rack C"]
    data = []
    for rack in racks:
        temp = random.uniform(22, 38)
        power = random.uniform(400, 900)
        workload = random.randint(60, 95)
        status = "⚠️ High" if temp > 35 or workload > 90 else "✅ Normal"
        data.append({
            "Rack": rack,
            "Temperature (°C)": round(temp, 1),
            "Power Draw (W)": round(power),
            "Workload (%)": workload,
            "Status": status
        })
    return pd.DataFrame(data)

df = generate_data()

# --- METRICS ---
col1, col2, col3 = st.columns(3)
col1.metric("Avg Temp", f"{df['Temperature (°C)'].mean():.1f} °C")
col2.metric("Total Power", f"{df['Power Draw (W)'].sum():.0f} W")
col3.metric("Peak Workload", f"{df['Workload (%)'].max()} %")

# --- HEATMAP / GRAPH VIEW ---
st.subheader("📊 Rack-wise Temperature Overview")
fig = px.bar(df, x="Rack", y="Temperature (°C)", color="Status", height=400)
st.plotly_chart(fig, use_container_width=True)

# --- TABLE VIEW ---
st.subheader("🔍 Detailed Rack Info")
st.dataframe(df, use_container_width=True)

# --- AI ALERTS & SUGGESTIONS ---
st.subheader("🤖 AI Alerts & Reinforcement Suggestions")
for index, row in df.iterrows():
    if row["Temperature (°C)"] > 35:
        st.warning(f"{row['Rack']} is overheating. 🔁 Reinforcement AI recommends increasing cooling by 15%.")
    if row["Workload (%)"] > 90:
        st.warning(f"{row['Rack']} nearing overload. 🔁 Suggest triggering workload migration.")

# --- CONTROL PANEL ---
st.subheader("🛠️ Operator Control Panel")
selected_rack = st.selectbox("Choose Rack to Control", df["Rack"].tolist())

if st.button("🌡️ Increase Cooling"):
    st.success(f"Cooling increased for {selected_rack} ✅")

if st.button("🔁 Trigger Workload Balancing"):
    st.success(f"Workload balancing initiated for {selected_rack} ✅")

# --- FOOTER ---
st.caption("Built with Streamlit | AI Edge Software Simulation for VC Demo")
