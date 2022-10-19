#!/usr/bin/python3
"""
<<<<<<< HEAD
Uses the JSON placeholder\
api to query data about an employee
=======
Uses the JSON placeholder api to query\
data about an employee
>>>>>>> ba58f479f0ec9a89d881d71c0d124b7d513408a2
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + "/user/{}/todos".format(argv[1])
    name_url = main_url + "/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_num = len(todo_result)
    todo_complete = len([todo for todo in todo_result
                         if todo.get("completed")])
    name = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_num))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
ist}, f)
