#!/usr/bin/python3
""" Task 0: Gather data from an API """

import requests
from sys import argv

def getTasks(id):
    """ Retrieve tasks for user """
    url = f'https://jsonplaceholder.typicode.com/todos?userId={id}'
    r = requests.get(url)
    if(r.status_code == 200):
        return r.json()
    return []

def getUser(id):
    """ Retrieve User info """
    url = f'https://jsonplaceholder.typicode.com/users/{id}'
    r = requests.get(url)
    if(r.status_code == 200):
        return r.json()

if __name__ == "__main__":
    if(len(argv) != 2):
        raise Exception("Invalid number of parameters")
    emp_id = int(argv[1])
    u = getUser(emp_id)
    if(u):
        done = 0
        total = 0
        task_list = getTasks(emp_id)
        if(len(task_list) > 0):
            total = len(task_list)
            done = list(task for task in task_list if task.get('completed') == True)
        print(f'Employee {u["name"]} is done with tasks({len(done)}/{total}):')
        for task in done:
            print(f'\t {task["title"]}')