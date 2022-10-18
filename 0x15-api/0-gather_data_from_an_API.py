#!/usr/bin/python3
# This script uses requests on a REST API to gather data about employee and thier tasks

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    end_point = "https://jsonplaceholder.typicode.com/"
    user = requests.get(end_point + 'users/{}'.format(user_id)).json()
    todos = requests.get(end_point + 'todos?userId={}'.format(user_id)).json()
    completed = []
    for todo in todos:
        if todo.get('completed') == True:
            completed.append(todo)
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), len(completed), len(todos)))
    for task in completed:
        print("\t{}".format(task.get('title')))
