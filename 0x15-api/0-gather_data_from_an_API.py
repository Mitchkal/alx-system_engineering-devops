#!/usr/bin/python3
""""
module 0-gather_data_from_an_API
gathers data from api
"""

import requests
import sys


def get_employee_todo_progress(emp_id):
    """
    gets and returns employee info
    starts with endpoint
    """

    api_url = f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}'

    response = requests.get(api_url)
    users = requests.get("http://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        todos = response.json()
        completed_tasks = [task for task in todos if task['completed']]
        comp_tasks = len(completed_tasks)
        total = len(todos)

        for user in users.json():
            if user.get('id') == int(emp_id):
                employee_name = user.get('name')
                break

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, comp_tasks, total))
        for task in completed_tasks:
            print("\t {}".format(task['title']))


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    get_employee_todo_progress(emp_id)
