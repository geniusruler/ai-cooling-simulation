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

# --- SIMULATED LOGIN UI (Disabled for demo purposes) ---
st.sidebar.header("🔐 Operator Panel")
user = st.sidebar.text_input("Username", "admin")
password = st.sidebar.text_input("Password", type="password")
st.sidebar.info("Login disabled for demo. Access granted ✅")

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


# --- ENERGY SAVINGS ESTIMATION ---
st.subheader("💰 Energy Savings Estimation (AI vs Traditional)")

baseline_power_per_rack = 1000  # Assumed constant power draw per rack in traditional control
num_racks = len(df)
ai_power_total = df["Power Draw (W)"].sum()

# Calculations
traditional_total_power = baseline_power_per_rack * num_racks
ai_daily_kwh = ai_power_total * 24 / 1000
traditional_daily_kwh = traditional_total_power * 24 / 1000
energy_saved_kwh = traditional_daily_kwh - ai_daily_kwh

# Costs
price_per_kwh = 0.12
daily_savings = energy_saved_kwh * price_per_kwh
yearly_savings = daily_savings * 365

# Display results
col_a, col_b, col_c = st.columns(3)
col_a.metric("Daily Energy Saved (kWh)", f"{energy_saved_kwh:.2f}")
col_b.metric("Daily Cost Savings", f"${daily_savings:.2f}")
col_c.metric("Yearly Projection", f"${yearly_savings:,.2f}")

st.caption("Estimates assume each traditional rack draws 1000W continuously and AI dynamically optimizes workloads and cooling.")

