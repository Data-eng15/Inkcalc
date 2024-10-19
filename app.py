from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/solve', methods=['POST'])
def solve():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    try:
        response = model.generate_content(f"Solve this math problem: {prompt}")
        return jsonify({'result': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)