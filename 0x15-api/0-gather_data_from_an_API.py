#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress."""

from requests import get
from sys import argv

if __name__ == "__main__":
    """Get id from the console"""
    id = int(argv[1])
    emp_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    task_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'

    emp_details = get(emp_url).json()
    total_tasks = get(task_url).json()

    completed_tasks = []
    for todo in total_tasks:
        if todo.get('completed') == True:
            completed_tasks.append(todo)

    print(
        f"Employee {emp_details.get('name')} is done with tasks({len(completed_tasks)}/{len(total_tasks)})")
    for todos in completed_tasks:
        print("\t{}".format(todos.get('title')))
