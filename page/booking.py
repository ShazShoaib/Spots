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
    st.title("Cuisines")
    for Cousine in Cuisines:
        cols = st.columns(25)
        with cols[1]:
            st.write(Cousine)

    