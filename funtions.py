import os

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a File"""
    if not os.path.isfile(filepath):
        with open(filepath, "w") as file:
            pass
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_write, filepath=FILEPATH):
    """Write a File"""
    with open(filepath, "w") as file_write:
        file_write.writelines(todos_write)
