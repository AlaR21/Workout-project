import streamlit as st
import pandas as pd
import numpy as np


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
else:    
    filtered_df = df
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

category = st.selectbox(
    "Select workout category:",
    df["category"].unique()
)

if category !="All":
    filtered_category_df = df[df["category"] == category]
    filtered_category_df = filtered_category_df.sort_values(by="activity", ascending=False)
    st.write(f"### Filtered Data for {category}")
    st.dataframe(filtered_category_df)

import numpy as np
import matplotlib.pyplot as plt

# grupowanie
activity_time = df.groupby('activity')['duration_min'].sum()

# zamiana na godziny
activity_hours = (activity_time / 60).round(2)

# kolory gradientowe
colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(activity_hours)))

# wykres
fig, ax = plt.subplots(figsize=(7, 4))

ax.bar(activity_hours.index, activity_hours.values, color=colors)

ax.set_title('Czas treningów wg aktywności')
ax.set_xlabel('Aktywność')
ax.set_ylabel('Godziny')
ax.tick_params(axis='x', rotation=45)

# pokazanie w Streamlit
st.pyplot(fig)
