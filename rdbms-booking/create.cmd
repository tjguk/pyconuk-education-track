IF EXIST bookings.db del bookings.db
sqlite3 bookings.db < create.sql
create-bookings.py
