#!python3
import os, sys
import sqlite3

db = sqlite3.connect("bookings.db")
q = db.cursor()

q.execute("INSERT INTO users (user_name) VALUES ('Tim Golden');")
q.execute("INSERT INTO users (user_name) VALUES ('Fred Smith');")

q.execute("INSERT INTO rooms (room_name) VALUES ('Room A');")
q.execute("INSERT INTO rooms (room_name) VALUES ('Room B');")

q.execute("""
INSERT INTO
    room_bookings
(
    room_id,
    user_id,
    booked_from,
    booked_to
)
SELECT
    (SELECT room_id FROM rooms WHERE room_name = 'Room A') AS room_id,
    (SELECT user_id FROM users WHERE user_name = 'Tim Golden') AS user_id,
    '2014-09-19 15:00' AS booked_from,
    '2014-09-19 15:59' AS booked_to
""")

q.close()
db.commit()
db.close()
