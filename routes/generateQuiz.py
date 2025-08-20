from flask import request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_quiz():
    try:
        data = request.get_json()
        print(data)
        topic = data.get("topic", "General Knowledge")
        num_questions = data.get("num_questions", 10)
        difficulty = data.get("difficulty", "medium")
        print(topic, num_questions, difficulty)
        prompt = f"""
        Generate {num_questions} multiple-choice quiz questions on the topic: "{topic}".
        Difficulty: {difficulty}.
        Format the response strictly as valid JSON in the following structure:
        {{
          "topic": "{topic}",
          "questions": [
            {{
              "question": "string",
              "options": ["A", "B", "C", "D"],
              "answer": "correct option",
              "explanation": "short explanation"
            }}
          ]
        }}
        """

        model = genai.GenerativeModel("gemini-2.5-pro")
        response = model.generate_content(prompt)
        print(response.text)
        
        # Parse the response as JSON
        import json
        try:
            quiz_data = json.loads(response.text)
            return jsonify(quiz_data)
        except json.JSONDecodeError as e:
            # If direct JSON parsing fails, try to extract JSON from markdown code blocks
            import re
            json_match = re.search(r'```(?:json\n)?(.*?)```', response.text, re.DOTALL)
            if json_match:
                quiz_data = json.loads(json_match.group(1))
                return jsonify(quiz_data)
            return jsonify({"error": "Failed to parse response from Gemini"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

