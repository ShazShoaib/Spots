import streamlit as st
import pandas as pd
import page.search as search
import page.booking as booking

st.set_page_config(layout="wide",initial_sidebar_state="collapsed",page_title="Spots")  # Enables wide mode

# if st.session_state doesnt exist, create it
if "Page" not in st.session_state:
    st.session_state["Page"] = "Search"
if "Spot" not in st.session_state:
    st.session_state["Spot"] = "Default"

st.markdown("""
        <style>
            section[data-testid="stSidebar"] {display: none;}
        </style>
    """, unsafe_allow_html=True)


if st.session_state["Page"] == "Search":
    search.search_page()
elif st.session_state["Page"] == "Booking":
    booking.booking_page()