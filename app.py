import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(
    page_title="Mental Health Dashboard",
    layout="wide"
)

# -------------------------------
# Load Data
# -------------------------------

@st.cache_data
def load_data():
    possible_paths = [
        os.path.join("data", "mental_health_survey_dataset_300k.csv"),
        "data/mental_health_survey_dataset_300k.csv",
        "mental_health_survey_dataset_300k.csv"
    ]
    
    df = None
    for path in possible_paths:
        if os.path.exists(path):
            df = pd.read_csv(path)
            break
            
    if df is None:
        st.error("❌ Dataset file nahi mili! Check karein ke file 'data' folder ke andar mojood hai.")
        st.stop()
        
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    if "survey_date" in df.columns:
        df["survey_date"] = pd.to_datetime(df["survey_date"])
        
    return df

df = load_data()

# -------------------------------
# Dashboard Title
# -------------------------------

st.title("Mental Health Analytics Dashboard")
st.markdown("Interactive dashboard for analyzing mental health survey data.")

# -------------------------------
# Sidebar Filters (Ab yeh shuru me khaali milenge)
# -------------------------------

st.sidebar.header("Filters")

# default=df["..."] hata diya hai taake list pehle se bhari hui na aaye
gender = st.sidebar.multiselect("Gender", df["gender"].unique())
country = st.sidebar.multiselect("Country", df["country"].unique())
occupation = st.sidebar.multiselect("Occupation", df["occupation"].unique())
risk = st.sidebar.multiselect("Mental Health Risk", df["mental_health_risk"].unique())

age_range = st.sidebar.slider(
    "Age Range",
    int(df["age"].min()),
    int(df["age"].max()),
    (int(df["age"].min()), int(df["age"].max()))
)

# -------------------------------
# Apply Filters (Smart Logic)
# -------------------------------
# Agar user ne kuch select nahi kiya, to hum saara data select rakhenge (taake charts khaali na hon)
# Aur jaise hi user kuch select karega, sirf wahi data filter ho jayega.

filtered_df = df[df["age"].between(age_range[0], age_range[1])]

if gender:
    filtered_df = filtered_df[filtered_df["gender"].isin(gender)]
if country:
    filtered_df = filtered_df[filtered_df["country"].isin(country)]
if occupation:
    filtered_df = filtered_df[filtered_df["occupation"].isin(occupation)]
if risk:
    filtered_df = filtered_df[filtered_df["mental_health_risk"].isin(risk)]

# -------------------------------
# KPI Cards
# -------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Records", f"{len(filtered_df):,}")
c2.metric("Avg Stress", round(filtered_df["stress_score"].mean(), 2) if "stress_score" in filtered_df.columns else 0)
c3.metric("Avg Anxiety", round(filtered_df["anxiety_score"].mean(), 2) if "anxiety_score" in filtered_df.columns else 0)
c4.metric("Avg Depression", round(filtered_df["depression_score"].mean(), 2) if "depression_score" in filtered_df.columns else 0)

st.divider()

# -------------------------------
# Pie Chart
# -------------------------------

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    filtered_df["gender"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    ax.set_title("Gender Distribution")
    st.pyplot(fig)

# -------------------------------
# Histogram
# -------------------------------

with col2:
    fig, ax = plt.subplots()
    sns.histplot(filtered_df["age"], bins=20, ax=ax)
    ax.set_title("Age Distribution")
    st.pyplot(fig)

# -------------------------------
# Bar Chart
# -------------------------------

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_df, x="mental_health_risk", ax=ax)
    ax.set_title("Mental Health Risk")
    st.pyplot(fig)

# -------------------------------
# Line Chart
# -------------------------------

with col2:
    if "survey_date" in filtered_df.columns and "stress_score" in filtered_df.columns:
        trend = filtered_df.groupby("survey_date")["stress_score"].mean()
        fig, ax = plt.subplots()
        trend.plot(ax=ax)
        ax.set_title("Average Stress Over Time")
        st.pyplot(fig)
    else:
        st.warning("Survey Date ya Stress Score column missing hai.")

# -------------------------------
# Scatter Plot
# -------------------------------

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_df, x="anxiety_score", y="depression_score", ax=ax)
    ax.set_title("Anxiety vs Depression")
    st.pyplot(fig)

# -------------------------------
# Box Plot
# -------------------------------

with col2:
    fig, ax = plt.subplots()
    sns.boxplot(y=filtered_df["stress_score"], ax=ax)
    ax.set_title("Stress Score Box Plot")
    st.pyplot(fig)

# -------------------------------
# Heatmap
# -------------------------------

st.subheader("Correlation Heatmap")

all_numeric_cols = [
    "age", "work_hours_per_week", "screen_time_hours", "sleep_hours", 
    "stress_score", "anxiety_score", "depression_score", 
    "academic_or_job_pressure", "financial_stress_score"
]
numeric_cols = [col for col in all_numeric_cols if col in filtered_df.columns]

if numeric_cols:
    corr = filtered_df[numeric_cols].corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
else:
    st.warning("Heatmap ke liye numerical columns nahi mile.")

# -------------------------------
# Area Chart
# -------------------------------

st.subheader("Sleep Hours Trend")
if "survey_date" in filtered_df.columns and "sleep_hours" in filtered_df.columns:
    sleep_trend = filtered_df.groupby("survey_date")["sleep_hours"].mean()
    st.area_chart(sleep_trend)

# -------------------------------
# Count Plot
# -------------------------------

st.subheader("Occupation Frequency")
fig, ax = plt.subplots(figsize=(12, 5))
sns.countplot(
    data=filtered_df,
    x="occupation",
    order=filtered_df["occupation"].value_counts().index,
    ax=ax
)
plt.xticks(rotation=45)
st.pyplot(fig)

# -------------------------------
# Violin Plot
# -------------------------------

st.subheader("Stress Distribution by Risk Level")
fig, ax = plt.subplots()
sns.violinplot(data=filtered_df, x="mental_health_risk", y="stress_score", ax=ax)
st.pyplot(fig)