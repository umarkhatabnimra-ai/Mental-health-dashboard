import streamlit as st

def apply_filters(df):

    st.sidebar.header("Filters")

    gender = st.sidebar.multiselect(
        "Gender",
        df["gender"].unique(),
        default=df["gender"].unique()
    )

    country = st.sidebar.multiselect(
        "Country",
        df["country"].unique(),
        default=df["country"].unique()
    )

    occupation = st.sidebar.multiselect(
        "Occupation",
        df["occupation"].unique(),
        default=df["occupation"].unique()
    )

    risk = st.sidebar.multiselect(
        "Mental Health Risk",
        df["mental_health_risk"].unique(),
        default=df["mental_health_risk"].unique()
    )

    age_range = st.sidebar.slider(
        "Age Range",
        int(df["age"].min()),
        int(df["age"].max()),
        (
            int(df["age"].min()),
            int(df["age"].max())
        )
    )

    filtered_df = df[
        (df["gender"].isin(gender))
        & (df["country"].isin(country))
        & (df["occupation"].isin(occupation))
        & (df["mental_health_risk"].isin(risk))
        & (df["age"].between(age_range[0], age_range[1]))
    ]

    return filtered_df