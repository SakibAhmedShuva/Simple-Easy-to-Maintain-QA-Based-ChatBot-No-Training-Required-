from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

# Get the directory where the script is running
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load the CSV file with Q&A
csv_file = os.path.join(base_dir, 'questions_answers.csv')
df = pd.read_csv(csv_file, encoding='ISO-8859-1')

# Extract questions, answers, and image paths
questions = df['Question'].tolist()
answers = df['Answer'].tolist()
images = df['Image'].tolist()

# Preprocess using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(questions)

# Function to find the best answer and corresponding image
def find_best_answer(user_query):
    # Preprocess user query and transform it into a vector
    user_query_vec = vectorizer.transform([user_query])
    
    # Calculate cosine similarity between the user query and all saved questions
    cosine_similarities = cosine_similarity(user_query_vec, tfidf_matrix).flatten()
    
    # Find the index of the most similar question
    best_match_index = np.argmax(cosine_similarities)
    
    # Return the answer and the image corresponding to the best match
    return answers[best_match_index], images[best_match_index]

# Flask route to handle API requests
@app.route('/chat-bot', methods=['POST'])
def get_answer():
    data = request.json
    user_query = data.get('query', '')
    
    if user_query:
        answer, image_filename = find_best_answer(user_query)
        # Generate the image URL
        if image_filename:
            image_url = url_for('static', filename=image_filename, _external=True)
            return jsonify({'query': user_query, 'answer': answer, 'image_url': image_url})
        return jsonify({'query': user_query, 'answer': answer})
    else:
        return jsonify({'error': 'No query provided'}), 400

# Main route
@app.route('/')
def index():
    return "Welcome to the Q&A API. Send a POST request to /api/get-answer with your query."

if __name__ == "__main__":
    app.run(debug=True)
