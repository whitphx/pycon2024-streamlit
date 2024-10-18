import streamlit as st

toggle_value = st.toggle("Click me!")

if toggle_value:
    st.markdown(":large_green_circle: ON")
else:
    st.markdown(":large_red_square: OFF")
