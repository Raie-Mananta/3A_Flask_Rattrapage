import uuid
from bookings_db import bookings_db

def get_all_bookings(offset=0, limit=10):
    bookings_list = list(bookings_db.values())
    return bookings_list[offset:offset + limit]

def get_booking_by_id(booking_id):
    return bookings_db.get(booking_id)

def create_booking(booking_data):
    booking_id = str(uuid.uuid4())
    new_booking = {"booking_id": booking_id, **booking_data}
    bookings_db[booking_id] = new_booking
    return new_booking

def update_booking(booking_id, booking_data):
    if booking_id in bookings_db:
        updated_booking = {"booking_id": booking_id, **booking_data}
        bookings_db[booking_id] = updated_booking
        return updated_booking
    else:
        return None

def delete_booking(booking_id):
    return bookings_db.pop(booking_id, None) is not None

def get_statistics_by_room_type():
    stats = {"SINGLE": 0, "DELUXE": 0, "SUITE": 0}
    for booking in bookings_db.values():
        if not booking["is_cancelled"]:
            room_type = booking["room_type"]
            if room_type in stats:
                stats[room_type] += 1
    return stats
