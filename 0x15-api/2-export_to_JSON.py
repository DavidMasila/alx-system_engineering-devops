#!/usr/bin/python3
"""Fetches information from a REST API and exports it in JSON format"""

from ast import arg
from json import dump
from requests import get
from sys import argv


if __name__ == "__main__":
    todo_url = f"https://jsonplaceholder.typicode.com/user/{argv[1]}/todos"
    empname_url = f"https://jsonplaceholder.typicode.com/user/{argv[1]}"

    todo_json = get(todo_url).json()
    empdatails_json = get(empname_url).json()

    todo_list = []
    for todo in todo_json:
        todo_dict = {}
        todo_dict.update({"task": todo.get("title"), "completed": todo.get(
            "completed"), "username": empdatails_json.get("username")})

        todo_list.append(todo_dict)

    
    with open(f"{argv[1]}.json","w", encoding="utf-8") as f:
        dump({argv[1]: todo_list}, f)
