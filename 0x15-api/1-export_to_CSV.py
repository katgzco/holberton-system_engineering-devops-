#!/usr/bin/python3
"""Returns information about given employee ID and TODO list progress.
    """
import csv
import requests
import sys

if __name__ == "__main__":

    completed_task = list()

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]
    username = user.get("name")

    with open("USER_ID.csv", mode='w') as file:
        file = csv.writer(file, delimiter=',',
                          quoting=csv.QUOTE_ALL)

        for task in todo:
            file.writerow([user_id, username, task.get(
                "completed"), task.get("title")])
