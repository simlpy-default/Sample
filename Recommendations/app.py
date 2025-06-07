import streamlit as st
import pandas as pd
st.write("Hello, Streamlit!")
# Load the hospital dataset
df = pd.read_csv("hospitals.csv")

# Set the title of the app
st.title("Hospital Recommendation System")

# Create a dropdown for selecting specialty
specialty = st.selectbox("Select Specialty", df['specialty'].unique())

# Create a dropdown for selecting city
city = st.selectbox("Select City", df['city'].unique())

# Button to trigger recommendations
if st.button("Recommend Hospitals"):
    # Filter the dataset based on selected specialty and city
    recommended = df[(df['specialty'] == specialty) & (df['city'] == city)]
    if not recommended.empty:
        st.write("Recommended Hospitals:")
        for idx, row in recommended.iterrows():
            st.write(f"{row['name']} - Rating: {row['rating']}")
    else:
        st.write("No hospitals found for the selected specialty and city.")
