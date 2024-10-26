from fastapi import FastAPI
import numpy as np
import time

app = FastAPI()

@app.get("/")
async def heavy_computation():
    start_time = time.time()

    # Example: matrix multiplication of large random matrices
    matrix_size = 300  # Adjust this for load
    A = np.random.rand(matrix_size, matrix_size)
    B = np.random.rand(matrix_size, matrix_size)
    result = np.dot(A, B)

    return {
        "message": f"Computation completed in {time.time() - start_time:.2f} seconds.",
        "matrix_result": result[0][0]
    }
