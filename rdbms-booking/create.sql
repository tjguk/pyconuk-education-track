CREATE TABLE
  users
(
    user_id INTEGER PRIMARY KEY,
    user_name VARCHAR(60)
)
;

CREATE TABLE
    rooms
(
    room_id INTEGER PRIMARY KEY,
    room_name VARCHAR(60)
)
;

CREATE TABLE
    room_bookings
(
    room_id INTEGER,
    user_id INTEGER,
    booked_at DATETIME
)
;
