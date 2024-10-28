import streamlit as st
import pandas as pd

st.title("Upload and Visualize CSV Data with Streamlit")

# File uploader for CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Display the visualization if the file is uploaded
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(data.head())

    st.line_chart(data, x="Date", y="Stock Price")
