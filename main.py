from sql import create_db, insert_bookmark
from text import text

print('Initializing.......')

# Execute control flow of program


def program():
    mode = input(text["get_mode"])
    # Mode 1: Add a new URL to the table (scrape url for data)
    if mode is '1':
        url = input(text["get_url"])
        insert_bookmark(url)
    # Mode 2: Print all bookmarks
    elif mode is '2':
        print('2')
    # Mode 3: Search bookmarks
    elif mode is '3':
        print('3')
    # Mode 4: Delete bookmark
    elif mode is '4':
        print('4')
    # Mode 5: Update bookmark
    elif mode is '5':
        print('5')
    else:
        print('Invalid Entry')


program()
