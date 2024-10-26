import streamlit as st
import time
import numpy as np

# Title of the app
st.title("Performance Test: Heavy Computation")

# Simulate heavy computation
def heavy_computation():
    st.write("Starting heavy computation...")
    start_time = time.time()

    # Example: matrix multiplication of large random matrices
    matrix_size = 300  # You can adjust this for different load levels
    A = np.random.rand(matrix_size, matrix_size)
    B = np.random.rand(matrix_size, matrix_size)
    result = np.dot(A, B)

    st.write(f"Computation completed in {time.time() - start_time:.2f} seconds.")
    st.write("Matrix multiplication result (first element):", result[0][0])


heavy_computation()
