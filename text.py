text = {
    "welcome": "Welcome to the python bookmark application. Follow the prompts to use.",
    "get_mode": '''
Select program mode:
\t1. Add a new bookmark.
\t2. Print all bookmarks.
\t3. Print one bookmark.
\t4. Delete a bookmark.
\t5. Update a bookmark.
\t6. Create DB.
\t7. Export current DB to CSV.
''',
    "help": "This is the help page.",
    "get_url": 'Enter url (or type "q" to quit): ',
    "open_url": 'Enter an id number to open in the browser (or type "q" to quit): ',
    "get_delete_id": 'Enter an id number to delete (or type "q" to quit): ',
    "continue?": 'Hit enter to continue or "q" to quit: ',
    "start_session": '''
    -------------------------------
    \tSession Started
    -------------------------------
    ''',
    "end_session": '''
    -------------------------------
    \tSession Closed
    -------------------------------
    ''',
    "print_one": 'Enter an id number to view details (or type "q" to quit): ',
}

sql = {
    "create_table": """ CREATE TABLE IF NOT EXISTS bookmarks (
                                        id integer PRIMARY KEY,
                                        url text NOT NULL,
                                        title text,
                                        site_name text,
                                        description text
                                    ); """,
    "create_bookmark": ''' INSERT INTO bookmarks(url, title, site_name, description)
                VALUES(?,?,?,?)''',
    "delete_by_id": 'DELETE FROM bookmarks WHERE id=?'
}
