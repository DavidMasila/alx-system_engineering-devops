#!/usr/bin/python3

"""exporting data obtained from 
REST API to csv
"""
from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv

if __name__ == '__main__':
    endpoint = 'https://jsonplaceholder.typicode.com'
    todo_url = endpoint + "/user/{}/todos".format(argv[1])
    empname_url = endpoint + "/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    empname_details = get(empname_url).json()

    todo_list = []
    for todo in todo_result:
        todo_dict = {}
        todo_dict.update({"USER_ID": argv[1], "USERNAME": empname_details.get(
            'username'), "TASK_COMPLETED_STATUS": todo.get("completed"), "TASK_TITLE": todo.get("title")})

        todo_list.append(todo_dict)

    with open('{}.csv'.format(argv[1]), "w", newline="" ) as f:
        header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(todo_list)
