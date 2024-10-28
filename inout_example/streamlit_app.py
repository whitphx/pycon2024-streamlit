import streamlit as st

# Core logic function
def process_data(number, text):
    transformed_number = number * 2
    uppercased_text = text.upper()
    return transformed_number, uppercased_text

# Streamlit UI setup
st.title("Data Processor")

# Input fields
number = st.number_input("Enter a number:", value=1)
text = st.text_input("Enter some text:")

# Button to execute the function
if st.button("Process"):
    # Call the core function with user inputs
    transformed_number, uppercased_text = process_data(number, text)

    # Display the outputs
    st.write("Transformed Number:", transformed_number)
    st.write("Uppercased Text:", uppercased_text)
