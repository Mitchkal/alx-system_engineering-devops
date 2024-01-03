#!/usr/bin/python3
""""
module 0-gather_data_from_an_API
gathers data from api export as json
"""

import json
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
        # completed_tasks = [task for task in todos if task['completed']]
        # comp_tasks = len(completed_tasks)
        # total = len(todos)
        # employee_name = 'Unknown'

        # for tasks in todos:
        for user in users.json():
            if user.get('id') == int(emp_id):
                employee_name = user.get('username')
                break

        # for user in users.json():
        # if user.get('id') == employee_id:
        # employee_name = user.get('username')

        tasks_list = []

        for task in todos:
            task_data = {

                    "task": task['title'],
                    "completed": str(task['completed']),
                    "username": employee_name
                    }
            tasks_list.append(task_data)

        result = {emp_id: tasks_list}
        json_data = json.dumps(result, indent=2)

        json_filename = f'{emp_id}.json'

        with open(json_filename, mode='w',
                  encoding='utf-8') as json_file:
            json_file.write(json_data)


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    get_employee_todo_progress(emp_id)
