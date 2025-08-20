from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from routes.generateQuiz import generate_quiz

# Load environment variables
load_dotenv()


# Initialize Flask
app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:8080", "http://127.0.0.1:8080"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route("/api/generateQuiz", methods=["POST"])
def generate_quiz_route():
    return generate_quiz()


if __name__ == "__main__":
    app.run(debug=True)
