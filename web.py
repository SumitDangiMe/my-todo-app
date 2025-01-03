import streamlit as st
import funtions
todos =funtions.get_todos()
def add_todo():
    todo1 = st.session_state["new_todo"]
    todos.append(todo1+"\n")
    funtions.write_todos(todos)



st.title("My todo App")
st.subheader("This is subheader")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        funtions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",
              placeholder="Add todo...",
              on_change=add_todo,key='new_todo')