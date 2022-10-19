#!/usr/bin/python3

"""
Uses requests to gather employee ID
and Todo items from REST API
Then exports the information to CSV
"""

from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv

if __name__ == "__main__":
    id = int(argv[1])
    emp_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    task_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'

    emp_details = get(emp_url).json()
    total_tasks = get(task_url).json()

    todo_list = []

    for todo in total_tasks:
        tasks_dict = {}
        tasks_dict.update({"USER_ID": id, "USERNAME": emp_details.get('username'), "TASK_COMPLETED_STATUS":
                          todo.get('completed'), "TASK_TITLE": todo.get('title')})
        todo_list.append(tasks_dict)

    with open(f"{id}.csv", "w", newline="") as f:
        fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = DictWriter(f, fieldnames=fields, quoting=QUOTE_ALL)
        writer.writerows(todo_list)
