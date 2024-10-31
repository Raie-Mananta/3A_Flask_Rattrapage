# main.py

from flask import Flask
from flask_cors import CORS
from controllers.booking_controller import booking_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(booking_bp)

@app.route("/", methods=["GET"])
def home():
    return {"message": "Bienvenue dans le sublime site de Nancy 'Mananta' ASTIER permettant de gérer des réservations."}, 200

if __name__ == "__main__":
    app.run(debug=True)
