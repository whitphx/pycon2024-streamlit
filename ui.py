import random
from PIL import Image
import requests

import streamlit as st

st.title('Awesome Streamlit app')

st.header("Data Visualizations")
st.markdown("Streamlit is a great tool to create visualizations")

st.subheader("Plotting")

st.area_chart({'data': [1, 5, 2, 6, 2, 1], 'data2': [10, 15, 12, 16, 12, 11]})

st.subheader("Maps")

st.map({"lat": [37.7749295, 35.6895, 34.052235], "lon": [-122.4194155, -139.6917, -118.243683]})

st.header("Dataframes")


st.write('Here is a simple dataframe')
st.dataframe({'A': [random.randint(0, 100) for _ in range(10)], 'B': [random.randint(0, 100) for _ in range(10)], 'C': [random.randint(0, 100) for _ in range(10)]})

st.header("Images")

image = Image.open(requests.get("https://picsum.photos/640/320", stream=True).raw)
st.image(image, caption='Random image from picsum.photos', use_column_width=True)
