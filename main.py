from create_db import create_db
from text import text

print('Initializing.......')


def program():
    mode = input(text["get_mode"])
    if mode is '1':
        print('1')
    elif mode is '2':
        print('2')
    elif mode is '3':
        print('3')
    elif mode is '4':
        print('4')
    elif mode is '5':
        print('5')
    else:
        print('Invalid Entry')


program()
