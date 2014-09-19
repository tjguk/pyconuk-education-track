from bottle import route, run, template

import sqlite3

SQLITE_FILEPATH = "bookings.db"

class Database(object):

    def __init__(self, filepath=SQLITE_FILEPATH):
        self.db = sqlite3.connect(filepath)

    def get_users(self, pattern="*"):
        q = self.db.cursor()
        try:
            q.execute("SELECT * FROM users WHERE user_name LIKE ?", [pattern.replace("*", "%")])
            return q.fetchall()
        finally:
            q.close()

@route('/users/')
def users(name=None):
    database = Database()
    html = """<html>
    <head>
    <title>Users</title>
    </head>
    <body>
    <h1>Users</h1>
    """

    html += "<ul>"
    for user_id, user_name in database.get_users():
        html += '<li id="user-%d">%s</li>' % (user_id, user_name)
    html += "</ul>"

    html += """
    </body>
    </html>
    """
    return html

@route("/")
def index():
    html = """<html>
    <head>
    <title>Booking Website</title>
    </head>
    <body>
    <p><a href="users/">Users</a></p>
    </body>
    </html>
    """
    return html

run(host='localhost', port=8080)