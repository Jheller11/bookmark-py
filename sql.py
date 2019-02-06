import sqlite3
from sqlite3 import Error
import requests
from bs4 import BeautifulSoup
import webbrowser
from prettytable import PrettyTable
import csv
from text import sql

db = "./db/bookmarks.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE sql
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_db():
    database = db
    sql_command = sql["create_table"]
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create bookmarks table
        create_table(conn, sql_command)
    else:
        print("Error! cannot create the database connection.")


def create_bookmark(conn, info):
    """ create a new item in bookmarks table
    :param conn:
    :param info:
    :return: bookmark id
    """
    sql_command = sql["create_bookmark"]
    cur = conn.cursor()
    cur.execute(sql_command, info)
    return cur.lastrowid


def insert_bookmark(url):
    database = db
    # fetch info from url
    res = requests.get(url)
    data = res.text
    soup = BeautifulSoup(data, 'html.parser')
    description = soup.find(
        'meta', property='og:description')
    site_name = soup.find(
        'meta', property='og:site_name')
    if description == None:
        description = 'Description not found.'
    else:
        description = description["content"]
    if site_name == None:
        site_name = 'Not found.'
    else:
        site_name = site_name["content"]
    bookmark = (url, soup.title.string,
                site_name, description)
    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new bookmark
        bookmark_id = create_bookmark(conn, bookmark)
        print(f"Bookmark successfully created at id: {bookmark_id}")


def select_all_bookmarks(conn):
    """
    Query all rows in the bookmarks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT id, title, site_name FROM bookmarks")
    rows = cur.fetchall()

    x = PrettyTable()
    x.field_names = ["ID", "title", "site name"]
    for row in rows:
        x.add_row(row)
    print(x)


def find_all_bookmarks():
    database = db
    # create a database connection
    conn = create_connection(database)
    with conn:
        print('All items: ')
        select_all_bookmarks(conn)


def select_one_bookmark(conn, num):
    """
    Query for a single row in bookmarks table
    :param conn: connection object
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookmarks WHERE id = ?", num)
    result = cur.fetchone()
    return result


def print_one_bookmark(num):
    database = db
    conn = create_connection(database)
    bookmark = select_one_bookmark(conn, num)
    if bookmark:
        print(f""" 
            -------------------------
            ID: {bookmark[0]}
            URL: {bookmark[1]}
            Title: {bookmark[2]}
            Site: {bookmark[3]}
            Desc.: {bookmark[4]}
            -------------------------
            """)
    else:
        print('Not Found')


def open_in_browser(num):
    # fetch url using id
    database = db
    conn = create_connection(database)
    with conn:
        site = select_one_bookmark(conn, num)
    # open in default browser
    webbrowser.open(site[1], 2)


def delete_bookmark(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM bookmarks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    print('Item deleted.')


def delete_bookmark_by_id(id):
    database = db
    conn = create_connection(database)
    with conn:
        delete_bookmark(conn, id)


def print_to_csv():
    database = db
    conn = create_connection(database)
    sql = 'SELECT * FROM bookmarks'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    outfile = open("./table.csv", "w")
    writer = csv.writer(outfile)
    writer.writerow(['ID', 'URL', 'Title', 'Site', 'Description'])
    writer.writerows(rows)
    outfile.close()
