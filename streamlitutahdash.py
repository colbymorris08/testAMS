import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("athlete_monitoring_data.csv", parse_dates=["Date"])

df = load_data()

# Sidebar - Athlete selection
athletes = df["Athlete"].unique()
selected_athlete = st.sidebar.selectbox("Select Athlete", athletes)

# Filtered data
athlete_data = df[df["Athlete"] == selected_athlete]

st.title("Athlete Monitoring Dashboard")
st.markdown(f"### Monitoring Trends for {selected_athlete}")

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
    st.subheader("📈 Trend Over Time")
    fig, ax = plt.subplots(figsize=(10, 5))
    for metric in selected_metrics:
        ax.plot(athlete_data["Date"], athlete_data[metric], label=metric)
    ax.set_xlabel("Date")
    ax.set_ylabel("Score")
    ax.legend()
    st.pyplot(fig)

# Correlation plot
st.subheader("📊 Correlation with Goals Added (G+)")
if selected_metrics:
    corr_data = athlete_data[selected_metrics + ['Goals Added (G+)']].dropna()
    correlations = corr_data.corr()['Goals Added (G+)'].drop('Goals Added (G+)')
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.barplot(x=correlations.values, y=correlations.index, ax=ax2)
    ax2.set_title("Correlation with Goals Added (G+)")
    ax2.set_xlabel("Pearson R")
    st.pyplot(fig2)
else:
    st.info("Please select at least one metric.")
