#!/usr/bin/python3
"""This script uses requests on a
REST API to gather data about employee and thier tasks
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    endpoint = 'https://jsonplaceholder.typicode.com'
    todo_url = endpoint + "/user/{}/todos".format(argv[1])
    empname_url = endpoint + "/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    empname_details = get(empname_url).json()

    todo_total = len(todo_result)
    todo_completed = len(
        [todo for todo in todo_result if todo.get("completed")])
    name = empname_details.get("name")
    print("Employee {} is done with tasks({}/{}):".format(name,
          todo_completed, todo_total))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
