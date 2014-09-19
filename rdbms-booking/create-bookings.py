#!python3
import os, sys
import sqlite3

db = sqlite3.connect("bookings.db")
q = db.cursor()

q.execute("INSERT INTO users (user_name) VALUES ('Tim Golden');")
q.execute("INSERT INTO users (user_name) VALUES ('Fred Smith');")

q.execute("INSERT INTO rooms (room_name) VALUES ('Room A');")
q.execute("INSERT INTO rooms (room_name) VALUES ('Room B');")

q.execute("SELECT * FROM users")
print(q.fetchall())
