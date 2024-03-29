#!/usr/bin/python3
""""
module 0-gather_data_from_an_API
gathers data from api
"""

import csv
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

        csv_filename = f'{emp_id}.csv'

        with open(csv_filename, mode='w', newline='',
                  encoding='utf-8') as csv_file:

            header = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            # csv_writer.writerow(header)

            for task in todos:
                data = [task['userId'], employee_name,
                        str(task['completed']), task['title']]
                csv_writer.writerow(data)

        # for task in completed_tasks:
        # print("\t {}".format(task['title']))


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    get_employee_todo_progress(emp_id)
