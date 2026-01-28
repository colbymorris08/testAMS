import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load data
@st.cache_data

def load_data():
    return pd.read_csv("athlete_monitoring_data.csv", parse_dates=["Date"])

df = load_data()

# Title styling
st.markdown("""
    <style>
    .main-title {
        font-size: 2.2em;
        font-weight: 800;
        color: #111827;
        padding-bottom: 0.5em;
    }
    .section-header {
        font-size: 1.5em;
        font-weight: 600;
        margin-top: 1.5em;
        color: #1f2937;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>⚽ Athlete Monitoring Dashboard</div>", unsafe_allow_html=True)

# Sidebar - Athlete selection
athletes = df["Athlete"].unique()
selected_athlete = st.sidebar.selectbox("Select Athlete", athletes)

# Filtered data
athlete_data = df[df["Athlete"] == selected_athlete]

st.markdown(f"<div class='section-header'>📈 Monitoring Trends for {selected_athlete}</div>", unsafe_allow_html=True)

# Monitoring metric options
metrics = [
    'Wellness Monitoring',
    'Heart Rate Monitoring',
    'Acoustic Myography (AMG)*',
    'SpO2 Monitoring*',
    'Blood Lactate Score',
    'Menstrual Cycle Tracking (Optional)',
    'GPS Tracking**',
    'Microdosed High-Intensity**',
    'Force Plate',
    'Fitness Score',
    'Workload Monitoring',
    'Biomechanics Evaluation',
    'Range of Motion Score'
]

# Select metrics
selected_metrics = st.multiselect("Select Metrics to Plot", metrics, default=metrics[:3])

# Line chart
if selected_metrics:
    st.markdown("<div class='section-header'>📊 Metric Trends Over Time</div>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10, 5))
    for metric in selected_metrics:
        ax.plot(athlete_data["Date"], athlete_data[metric], label=metric)
    ax.set_xlabel("Date")
    ax.set_ylabel("Score")
    ax.legend()
    st.pyplot(fig)
else:
    st.info("Please select at least one metric to view trends.")

# Customizable regression scatter plot
st.markdown("<div class='section-header'>📉 Custom Variable Relationship Explorer</div>", unsafe_allow_html=True)

# All numeric columns for plotting
numeric_cols = df.select_dtypes(include=["float", "int"]).columns.tolist()

x_axis = st.selectbox("Select X-axis Variable", numeric_cols, index=numeric_cols.index("Front Knee Extension Change from FP to BR") if "Front Knee Extension Change from FP to BR" in numeric_cols else 0)
y_axis = st.selectbox("Select Y-axis Variable", numeric_cols, index=numeric_cols.index("Goals Added (G+)") if "Goals Added (G+)" in numeric_cols else 1)

# Filter out missing values
scatter_data = df[[x_axis, y_axis]].dropna()
X = scatter_data[[x_axis]].values
y = scatter_data[y_axis].values

# Fit linear regression
model = LinearRegression().fit(X, y)
y_pred = model.predict(X)
r_squared = r2_score(y, y_pred)

# Plot
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.scatter(X, y, color='black', alpha=0.6, s=30)
ax2.plot(X, y_pred, color='orange', linewidth=2)
ax2.set_xlabel(x_axis)
ax2.set_ylabel(y_axis)
ax2.set_title(f"{y_axis} vs {x_axis}\nR² = {r_squared:.3f}")
st.pyplot(fig2)
