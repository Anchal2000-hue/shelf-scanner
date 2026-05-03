import sys
sys.path.insert(0, 'E:/pypackages')

from flask import Flask, render_template, jsonify, request
from groq import Groq
from dotenv import load_dotenv
import os
import base64
import json

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    image_data = data.get('image')

    if not image_data:
        return jsonify({'error': 'No image provided'})

    # Remove base64 header
    if ',' in image_data:
        image_data = image_data.split(',')[1]

    prompt = """You are a book expert. Look at this bookshelf image carefully.

Identify ALL visible books and return a JSON response with exactly this format:
{
  "books": [
    {
      "title": "Book Title",
      "author": "Author Name",
      "genre": "Genre",
      "summary": "One sentence summary",
      "rating": 4.5,
      "recommended": true,
      "reason": "Why this book is recommended"
    }
  ],
  "total_found": 5,
  "recommendation": "Overall reading recommendation based on the collection"
}

Return only valid JSON, no other text, no markdown, no backticks."""

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ],
        max_tokens=2000,
        temperature=0.3
    )

    result = json.loads(response.choices[0].message.content)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)