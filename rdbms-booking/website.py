from bottle import route, run, template

import sqlite3

SQLITE_FILEPATH = "bookings.db"

class Database(object):

    def __init__(self, filepath=SQLITE_FILEPATH):
        self.db = sqlite3.connect(filepath)

    def get_user(self, user_id):
        q = self.db.cursor()
        try:
            q.execute("SELECT * FROM users WHERE user_id = ?", [user_id])
            for user in q.fetchall():
                return user
        finally:
            q.close()

    def get_room(self, room_id):
        q = self.db.cursor()
        try:
            q.execute("SELECT * FROM rooms WHERE room_id = ?", [room_id])
            for room in q.fetchall():
                return room
        finally:
            q.close()

    def get_users(self, pattern="*"):
        q = self.db.cursor()
        try:
            q.execute("SELECT * FROM users WHERE user_name LIKE ?", [pattern.replace("*", "%")])
            return q.fetchall()
        finally:
            q.close()

    def get_user_bookings(self, user_id):
        q = self.db.cursor()
        try:
            q.execute("""
            SELECT
                roo.*
            FROM
                rooms AS roo
            JOIN room_bookings AS rbo ON
                rbo.room_id = roo.room_id
            WHERE rbo.user_id = ?
            """, [user_id])
            return q.fetchall()
        finally:
            q.close()

    def get_room_bookings(self, room_id):
        q = self.db.cursor()
        try:
            q.execute("""
            SELECT
                usr.*
            FROM
                users AS usr
            JOIN room_bookings AS rbo ON
                rbo.user_id = usr.user_id
            WHERE rbo.room_id = ?
            """, [room_id])
            return q.fetchall()
        finally:
            q.close()

@route('/users/<id>/bookings')
def user_bookings(id):
    database = Database()
    user_id, user_name = database.get_user(id)
    title = "Bookings for %s" % user_name
    html = """<html>
    <head>
    <title>%s</title>
    </head>
    <body>
    <h1>%s</h1>
    """ % (title, title)

    html += "<ul>"
    for room_id, room_name in database.get_user_bookings(user_id):
        html += '<li><a href="/rooms/%d/bookings">%s</a></li>' % (room_id, room_name)
    html += "</ul>"

    html += """
    </body>
    </html>
    """
    return html

@route('/rooms/<id>/bookings')
def room_bookings(id):
    database = Database()
    room_id, room_name = database.get_room(id)
    title = "Bookings for %s" % room_name
    html = """<html>
    <head>
    <title>%s</title>
    </head>
    <body>
    <h1>%s</h1>
    """ % (title, title)

    html += "<ul>"
    for user_id, user_name in database.get_room_bookings(room_id):
        html += '<li><a href="/users/%d/bookings">%s</a></li>' % (user_id, user_name)
    html += "</ul>"

    html += """
    </body>
    </html>
    """
    return html

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
        html += '<li id="user-%d"><a href="/users/%d/bookings">%s</a></li>' % (user_id, user_id, user_name)
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