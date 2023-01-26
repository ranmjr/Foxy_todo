import time

import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.image("foxy_icon.PNG")
st.write("\n\n\n")

st.title("Foxy todo list")
st.subheader("The original foxy productivity app")

st.write("\n\n\n")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add a new task...",
              on_change=add_todo, key="new_todo")

st.write("\n\n\n")

if st.button("Play the foxy tune", key="tune"):
    st.audio("Fox_todo.mp3")

st.write("\n\n\n")

if st.button("Generate a random foxy quote", key="quote"):
    fox_quote = st.empty()
    fox_quote.subheader(':blue["]' + f":blue[{functions.get_quote()}]" + ':blue["]')
    time.sleep(3)
    fox_quote.subheader("")











