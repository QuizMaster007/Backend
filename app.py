from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from routes.generateQuiz import generate_quiz
from routes.readImage import read_image
# Load environment variables
load_dotenv()


# Initialize Flask
app = Flask(__name__)
CORS(app)

@app.route("/api/generateQuiz", methods=["POST"])
def generate_quiz_route():
    return generate_quiz()

@app.route("/api/readImage", methods=["POST"])
def read_image_route():
    return read_image()

if __name__ == "__main__":
    app.run(debug=True)
