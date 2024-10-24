import streamlit as st

toggle_value = st.toggle("Click me!")

if toggle_value:
    st.markdown("ON")
else:
    st.markdown("OFF")
