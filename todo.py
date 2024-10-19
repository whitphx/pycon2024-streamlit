import streamlit as st

# tasks = []   # ⚠️ Doesn't work.
if "tasks" not in st.session_state:
    st.session_state.tasks = []
tasks = st.session_state.tasks

new_task_name = st.text_input("Task Name")
if new_task_name:
    tasks.append(new_task_name)

st.write("## Tasks")
for task in tasks:
    st.write(task)
