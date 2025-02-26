import streamlit as st
import pandas as pd
from page.search import load_data



def booking_page():
    df = load_data()

    if st.button("<- Look at other Spots"):
        st.session_state["Page"] = "Search"
        st.rerun()
        
    st.title(st.session_state["Spot"])
    st.image(f"Images/{st.session_state['Spot']}.jpg")
    st.write(df[df['Name'] == st.session_state["Spot"]]['Description'].values[0])
    Cuisines = df.loc[df["Name"] == st.session_state["Spot"], "Cuisine"].iloc[0]
    Cuisines = Cuisines.split(":")
    # st.title("Cuisines")
    # for Cousine in Cuisines:
    #     cols = st.columns(25)
    #     with cols[1]:
    #         st.write(Cousine)
    st.write("Book a Table Now")

    cols = st.columns([0.33,0.33,0.33])
    with cols[0]:
        party_size = st.selectbox("Party", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    with cols[1]:
        party_date = st.date_input("Date")
    with cols[2]:
        party_time = st.selectbox("Time", ["12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM", "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM", "6:00 PM", "6:30 PM", "7:00 PM", "7:30 PM", "8:00 PM", "8:30 PM", "9:00 PM", "9:30 PM", "10:00 PM", "10:30 PM", "11:00 PM", "11:30 PM"])


    if st.button("Book Now"):
        st.write(f"Table Booked for {party_size} on {party_date} at {party_time}")

