from locust import HttpUser, TaskSet, task, between
import requests
import websocket
import threading
from streamlit.proto import BackMsg_pb2, ClientState_pb2, ForwardMsg_pb2

STREAMLIT_URL = "http://localhost:8501"
WEBSOCKET_URL = "ws://localhost:8501/_stcore/stream"

class StreamlitUserBehavior(TaskSet):
    def on_start(self):
        """On start, make an HTTP request to the main page and establish a WebSocket connection."""
        # 1. Access the main page ("/") via HTTP
        response = self.client.get("/")
        print(f"HTTP Response status code: {response.status_code}")

        # 2. Establish WebSocket connection
        self.ws = websocket.create_connection(WEBSOCKET_URL)
        print("WebSocket connection established.")

        # 3. Send the initial rerun request
        msg = BackMsg_pb2.BackMsg(
            rerun_script=ClientState_pb2.ClientState()
        )
        buffer = msg.SerializeToString()
        self.ws.send(buffer, websocket.ABNF.OPCODE_BINARY)

    @task
    def interact_with_websocket(self):
        """Listen to WebSocket messages and handle `script_finished`."""
        try:
            # Receive messages until the script has finished running
            while True:
                result = self.ws.recv()
                forward_msg = ForwardMsg_pb2.ForwardMsg()
                forward_msg.ParseFromString(result)
                print(f"Received -> {forward_msg}")

                # Exit loop if script is finished
                if forward_msg.WhichOneof("type") == "script_finished":
                    break

        except Exception as e:
            print(f"WebSocket error: {e}")

    def on_stop(self):
        """Close the WebSocket connection when the user stops."""
        self.ws.close()
        print("WebSocket connection closed.")

class StreamlitUser(HttpUser):
    tasks = [StreamlitUserBehavior]
    wait_time = between(1, 3)  # Simulate random wait time between tasks
