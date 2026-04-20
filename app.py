import streamlit as st
import pandas as pd

st.title("Workout Natalia's Tracker")

df = pd.read_csv('activities_enhanced_400.csv')

st.write("### Raw Data Preview")

df["distance_km"] = df["distance_km"].fillna(0)

st.dataframe(df.head(50))

activity = st.selectbox(
    "Select an activity type:",
    df["activity"].unique()
)

if activity!="All":
    filtered_df = df[df["activity"] == activity]
    st.write(f"### Filtered Data for {activity}")
    st.dataframe(filtered_df)

st.write("### Top calorie-burning activity per category")
top_df = filtered_df.loc[filtered_df.groupby("activity")["kcal"].idxmax()]


for _, row in top_df.iterrows():   #zwraca kazdy wiersz z DataFrame jako Series, gdzie _ to indeks, a row to zawartość wiersza
    st.markdown(f"""   
    **{row['activity']}**  
    Duration: {row['duration_min']} min  
    Calories: {row['kcal']} kcal  
    Intensity: {row['intensity']}
    """)

