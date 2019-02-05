import sqlite3
from sqlite3 import Error


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
    database = "./db/bookmarks.db"
    sql_create_bookmarks_table = """ CREATE TABLE IF NOT EXISTS bookmarks (
                                        id integer PRIMARY KEY,
                                        url text NOT NULL,
                                        title text
                                    ); """
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create bookmarks table
        create_table(conn, sql_create_bookmarks_table)
    else:
        print("Error! cannot create the database connection.")


def create_bookmark(conn, info):
    """ create a new item in bookmarks table
    :param conn:
    :param info:
    :return: bookmark id
    """
    sql = ''' INSERT INTO bookmarks(url, title)
                VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, info)
    return cur.lastrowid


def insert_bookmark(url):
    database = "./db/bookmarks.db"
    # fetch info from url

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new bookmark
        bookmark_id = create_bookmark(conn, bookmark)
        print(f"Bookmark successfully created at id: {bookmark_id}")
