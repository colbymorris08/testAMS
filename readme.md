# ⚽ Athlete Monitoring Dashboard

An interactive Streamlit dashboard for athlete monitoring, performance analysis, and development tracking across youth and professional environments.

This tool is designed to help performance staff, coaches, and analysts **visualize trends, explore relationships between metrics, and differentiate priorities between youth development and professional performance**.

---

## 🚀 Features

### 📈 Athlete Monitoring Trends
- Time-series visualization of key athlete monitoring metrics
- Multi-metric overlay to identify patterns, spikes, and fatigue signals
- Athlete-specific filtering for individualized analysis

### 📊 Metrics Supported
- Wellness Monitoring  
- Heart Rate Monitoring  
- Acoustic Myography (AMG)  
- SpO₂ Monitoring  
- Blood Lactate  
- Menstrual Cycle Tracking (optional)  
- GPS Tracking  
- Micro-dosed High-Intensity Load  
- Force Plate Metrics  
- Workload Monitoring  
- Biomechanics Evaluation  
- Range of Motion Scores  
- Composite Fitness Scores  

### 📉 Relationship Explorer (Regression Tool)
- Custom X vs Y variable selection
- Linear regression fit with R² evaluation
- Quickly test hypotheses (e.g., biomechanics vs performance outputs)

---

## 🧠 Applied Framework: Youth vs Pro Focus

### 🧒 Youth / Academy Athletes
Primary emphasis:
- **Skill acquisition**
- **Biomechanical adaptation**
- **Movement quality**
- **Long-term athletic development**

Monitoring is used to:
- Track growth-related changes
- Identify coordination and mobility adaptations
- Guide training progressions, not game output

### 🧑‍💼 Professional Athletes
Primary emphasis:
- **Match performance**
- **Injury mitigation**
- **Fatigue management**
- **Availability over volume**

Monitoring is used to:
- Detect overload and recovery needs
- Optimize weekly load around competition
- Preserve performance across congested schedules

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit**
- **Pandas / NumPy**
- **Matplotlib**
- **scikit-learn**

---

## 📂 Data Requirements
The app expects a CSV file named:
athlete_monitoring_data.csv
This csv is currently SIMULATED data, meanth to serve as an example for what an operational dash would look like.
Required columns:
- `Date` (datetime)
- `Athlete` (string)
- Monitoring and performance metrics (numeric)

