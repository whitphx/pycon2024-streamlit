import requests
import websocket
from threading import Thread

from streamlit.proto import BackMsg_pb2, ClientState_pb2, ForwardMsg_pb2

STREAMLIT_URL = "http://localhost:8501"
WEBSOCKET_URL = "ws://localhost:8501/_stcore/stream"

# Function to simulate a single user
def simulate_user(user_id):
    # 1. Access the main page ("/")
    response = requests.get(STREAMLIT_URL)
    print(f"User {user_id}: HTTP Response status code: {response.status_code}")

    # 2. Establish WebSocket connection
    ws = websocket.create_connection(WEBSOCKET_URL)
    print(f"User {user_id}: WebSocket connection established.")

    msg = BackMsg_pb2.BackMsg(
        rerun_script=ClientState_pb2.ClientState()
    )
    buffer = msg.SerializeToString()
    ws.send(buffer, websocket.ABNF.OPCODE_BINARY)

    while True:
        result = ws.recv()
        forward_msg = ForwardMsg_pb2.ForwardMsg()
        forward_msg.ParseFromString(result)
        print(f"User {user_id}: Received -> {forward_msg}")

        if forward_msg.WhichOneof("type") == "script_finished":
            break

    ws.close()
    print(f"User {user_id}: WebSocket connection closed.")

# Function to run multiple users concurrently
def run_load_test(num_users):
    threads = []
    for i in range(num_users):
        thread = Thread(target=simulate_user, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    NUM_USERS = 10  # Number of concurrent users to simulate
    run_load_test(NUM_USERS)
