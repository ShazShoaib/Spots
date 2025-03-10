import streamlit as st
import pandas as pd
from rapidfuzz import process, fuzz  # Efficient fuzzy matching

@st.cache_data
def load_data():
    # Load CSV (Ensure the file exists in your working directory)
    return pd.read_csv('spots.csv', encoding='ISO-8859-1')

def get_cuisine_icon(cuisine):
    cuisine_icons = {
        "Italian": "🍕",
        "Japanese": "🍣",
        "Steakhouse": "🥩",
        "Chinese": "🍜",
        "Vegetarian": "🥗",
        "American": "🍔",
        "Mexican": "🌮",
        "Indian": "🍛",
        "Middle Eastern": "🥘",
        "Seafood": "🍤"
    }
    
    return cuisine_icons.get(cuisine, "❓")  # Default to ❓ if cuisine is not found


def search_page():

    st.markdown(
        "<h1 style='text-align: center; font-size: 100px; color: #EC1313;'>SPOTS</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align: center; font-size: 25px;'>Find your SPOT now!</h3>",
        unsafe_allow_html=True
    )

    search = st.text_input('Search for your Spot')



    df = load_data()

    # Icons for food categories (extra slots added for safety)
    icons = ["🍕", "🍣", "🥩", "🍜", "🥗", "🍔", "🌮", "🍛", "🥘", "🍤"]

    # Reorder df based on search similarity
    if search:
        names = df['Name'].tolist()
        matches = process.extract(search, names, scorer=fuzz.partial_ratio, limit=len(names))
        matched_names = [match[0] for match in matches]
        df = df.set_index('Name').loc[matched_names].reset_index()  # Reorder df

    # Iterate through the reordered DataFrame
    for _, row in df.iterrows():
        with st.container():
            st.markdown("---")  # Separator for visual clarity
            st.write(f"### 🍽️ {row['Name']}")  # Restaurant name
            st.image(f"Images/{row['Name']}.jpg")
            st.write(f"📖 {row['Description']}")  # Description
            
            # Split cuisines and ensure exactly 7 slots
            cuisines = row["Cuisine"].split(":")
            cuisines += [""] * (7 - len(cuisines))  # Fill empty slots

            # Fixed 7-column layout for cuisines
            for cuisine, icon in zip(cuisines, icons):
                icon = get_cuisine_icon(cuisine)
                if cuisine:  # Only display if cuisine exists
                    st.write(f"{icon} **{cuisine}**")


        st.markdown(
            """
            <style>
            div.stButton > button:first-child {
                background-color: red !important;
                color: white !important;
                border-radius: 5px;
                border: none;
                transition: 0.3s ease-in-out;
            }

            div.stButton > button:first-child:hover {
                outline: 2px solid white !important;
                background-color: darkred !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )




        # Unique key for each button (use row index to avoid errors)
        if st.button("Book Now", key=f"book_{row['Name']}"):



            st.session_state["Spot"] = row['Name']
            st.session_state["Page"] = "Booking"
            st.rerun()

