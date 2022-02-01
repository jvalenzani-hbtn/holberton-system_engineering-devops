#!/usr/bin/python3
""" Task 1: Export to CSV """

import requests
from sys import argv

def getTasks(id):
    """ Retrieve tasks for user """
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
    r = requests.get(url)
    if(r.status_code == 200):
        return r.json()
    return []

def getUser(id):
    """ Retrieve User info """
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    r = requests.get(url)
    if(r.status_code == 200):
        return r.json()

if __name__ == "__main__":
    if(len(argv) != 2):
        raise Exception("Invalid number of parameters")
    emp_id = int(argv[1])
    u = getUser(emp_id)
    if(u):
        with open(f'{emp_id}.csv', 'w+') as data_file:
            task_list = getTasks(emp_id)
            if(len(task_list) > 0):
                for task in task_list:
                    data_file.write('"{}","{}","{}","{}"\n'.format(u["id"],u["username"],task["completed"],task["title"]))