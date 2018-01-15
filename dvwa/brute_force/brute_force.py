#!/usr/bin/env python3

import requests


passwords = ['admin', 'admin1', 'admin.1', 'pass', 'password']

session = requests.Session()

login_response = session.post(
    'http://localhost/login.php',
    data={
        'Login': 'Login',
        'username': 'admin',
        'password': 'password'
    }
)

import ipdb; ipdb.set_trace()

task_response = session.get(
    'http://localhost/vulnerabilities/brute/',
    data={'Login': 'Login', 'username': 'admin', 'password': 'password'},
    cookies=session.cookies
)

task_response = session.get(
    'http://localhost/vulnerabilities/brute/',
    data={'Login': 'Login', 'username': 'admin', 'password': 'password'},
    cookies=session.cookies
)

print(task_response.content)
