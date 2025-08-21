from flask import request, jsonify
import pytesseract
from PIL import Image

def read_image():
    """
    Receive an uploaded image from the user,
    extract text using Tesseract OCR, and return as JSON.
    """
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files["image"]

    try:
        # Open image directly from memory (no saving)
        img = Image.open(file.stream)

        # Extract text
        text = pytesseract.image_to_string(img).strip()

        return jsonify({"extracted_text": text})

    except Exception as e:
        return jsonify({"error": f"Error processing image: {e}"}), 500
