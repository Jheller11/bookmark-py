# Python Bookmarks Script

## Description

This script accepts a user input url and scrapes the corresponding page, then stores the url, site name, description, and title in a sqlite db.

The table can then be exported to a .csv or printed directly in the terminal. After printing, users can specify an id number and open that page directly in their default web browser.

## Version

Python 3.7.1

## Packages

1. requests
2. bs4
3. prettytable

## Code Sample

I am currently working on improving this section of code, which takes a url as input and uses the BeautifulSoup and requests packages to find a parse the other info that I want to store in the table.

```
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

```
