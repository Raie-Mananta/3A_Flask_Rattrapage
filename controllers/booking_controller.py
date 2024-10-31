
from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
from services.booking_service import (
    get_all_bookings, get_booking_by_id, create_booking,
    update_booking, delete_booking, get_statistics_by_room_type
)

booking_bp = Blueprint("booking", __name__)

booking_schema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "string"},
        "start_date": {"type": "string"},
        "end_date": {"type": "string"},
        "is_cancelled": {"type": "boolean"},
        "is_paid": {"type": "boolean"},
        "price": {"type": "number", "minimum": 0},
        "room_type": {"type": "string", "enum": ["SINGLE", "DELUXE", "SUITE"]}
    },
    "required": ["user_id", "start_date", "end_date", "is_cancelled", "is_paid", "price", "room_type"],
    "additionalProperties": False
}

@booking_bp.route("/bookings", methods=["GET"])
def get_bookings():
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))
    bookings = get_all_bookings(offset, limit)
    return jsonify(bookings), 200

@booking_bp.route("/bookings/<string:booking_id>", methods=["GET"])
def get_booking(booking_id):
    booking = get_booking_by_id(booking_id)
    if booking:
        return jsonify(booking), 200
    else:
        return jsonify({"error": "Reservation not found"}), 404

@booking_bp.route("/bookings", methods=["POST"])
@expects_json(booking_schema)
def create_new_booking():
    booking_data = request.json
    new_booking = create_booking(booking_data)
    return jsonify(new_booking), 201

@booking_bp.route("/bookings/<string:booking_id>", methods=["PUT"])
@expects_json(booking_schema)
def update_existing_booking(booking_id):
    booking_data = request.json
    updated_booking = update_booking(booking_id, booking_data)
    if updated_booking:
        return jsonify(updated_booking), 200
    else:
        return jsonify({"error": "Reservation not found"}), 404

@booking_bp.route("/bookings/<string:booking_id>", methods=["DELETE"])
def delete_existing_booking(booking_id):
    success = delete_booking(booking_id)
    if success:
        return '', 204
    else:
        return '', 204 
    
@booking_bp.route("/statistics/room_type", methods=["GET"])
def room_type_statistics():
    stats = get_statistics_by_room_type()
    return jsonify(stats), 200
