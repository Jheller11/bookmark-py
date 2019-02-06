from sql import create_db, insert_bookmark, find_all_bookmarks, open_in_browser, delete_bookmark_by_id, print_to_csv
from text import text

print(text['start_session'])

print(text["welcome"])

# Execute control flow of program


def main():
    mode = input(text["get_mode"])
    # Mode 1: Add a new URL to the table (scrape url for data)
    if mode is '1':
        url = input(text["get_url"])
        if url == "q":
            pass
        else:
            insert_bookmark(url)
    # Mode 2: Print all bookmarks
    elif mode is '2':
        find_all_bookmarks()
        # ask user if they want to open a link in browser by id
        user_input = input(text["open_url"])
        if user_input == 'q':
            pass
        else:
            open_in_browser(user_input)
    # Mode 3: Search bookmarks
    elif mode is '3':
        print('3')
    # Mode 4: Delete bookmark
    elif mode is '4':
        user_input = input(text["get_delete_id"])
        if user_input == 'q':
            pass
        else:
            delete_bookmark_by_id(user_input)
    # Mode 5: Update bookmark
    elif mode is '5':
        print('5')
    elif mode is '6':
        create_db()
    elif mode is '7':
        print_to_csv()
    else:
        print('Invalid Entry')

    # restart program or quit based on user input
    user_input = input(text["continue?"])
    if user_input is '':
        main()
    else:
        pass


main()

print(text['end_session'])
