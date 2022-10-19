#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

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
