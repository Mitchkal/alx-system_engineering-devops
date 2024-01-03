#!/usr/bin/python3
""""
module 0-gather_data_from_an_API
gathers data from api export as json
"""

import json
import requests


def get_employee_todo_progress():
    """
    gets and returns employee info for all employees
    starts with endpoint
    """
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    employees = users.json()

    all_users_data = []

    for user in employees:
        emp_id = user.get('id')
        api_url = f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}'

        response = requests.get(api_url)

        if response.status_code == 200:
            todos = response.json()
            employee_name = user.get('username')
            tasks_list = []

            for task in todos:
                task_data = {
                        "task": task['title'],
                        "completed": (task['completed']),
                        "username": employee_name
                        }
                tasks_list.append(task_data)

            result = {emp_id: tasks_list}
            all_users_data.append(result)

    json_data = json.dumps(all_users_data, separators=(',', ': '))

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json_file.write(json_data)


if __name__ == "__main__":
    get_employee_todo_progress()
