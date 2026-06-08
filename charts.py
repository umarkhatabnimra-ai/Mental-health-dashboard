import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def gender_pie(df):

    fig, ax = plt.subplots()

    df["gender"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_title("Gender Distribution")
    ax.set_ylabel("")

    st.pyplot(fig)

    st.info("""
    Description:
    This pie chart shows the percentage distribution
    of genders in the dataset.
    """)


def age_histogram(df):

    fig, ax = plt.subplots()

    sns.histplot(
        df["age"],
        bins=20,
        ax=ax
    )

    ax.set_title("Age Distribution")

    st.pyplot(fig)

    st.info("""
    Description:
    This histogram shows the age distribution
    of survey participants.
    """)


def risk_bar(df):

    fig, ax = plt.subplots()

    sns.countplot(
        data=df,
        x="mental_health_risk",
        ax=ax
    )

    ax.set_title("Mental Health Risk")

    st.pyplot(fig)

    st.info("""
    Description:
    Shows the number of people in each
    mental health risk category.
    """)


def anxiety_depression_scatter(df):

    fig, ax = plt.subplots()

    sns.scatterplot(
        data=df,
        x="anxiety_score",
        y="depression_score",
        ax=ax
    )

    ax.set_title("Anxiety vs Depression")

    st.pyplot(fig)

    st.info("""
    Description:
    Displays relationship between anxiety
    and depression scores.
    """)


def stress_boxplot(df):

    fig, ax = plt.subplots()

    sns.boxplot(
        y=df["stress_score"],
        ax=ax
    )

    ax.set_title("Stress Score Box Plot")

    st.pyplot(fig)

    st.info("""
    Description:
    Shows spread, median and outliers
    of stress scores.
    """)


def correlation_heatmap(df):

    numeric_cols = [
        "age",
        "work_hours_per_week",
        "screen_time_hours",
        "sleep_hours",
        "stress_score",
        "anxiety_score",
        "depression_score",
        "academic_or_job_pressure",
        "financial_stress_score"
    ]

    fig, ax = plt.subplots(figsize=(10,6))

    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

    st.info("""
    Description:
    Shows correlation between numerical features.
    """)