# Simple Q&A Chatbot Flask API with html Template (no training required)

This repository contains a simple and efficient Q&A chatbot built using Flask (backend) and a web interface (frontend). The bot uses TF-IDF and cosine similarity to match user queries with predefined questions and provide corresponding answers and images.

## Features

- **No training required**: The chatbot operates using TF-IDF and cosine similarity without the need to train any machine learning model.
- **Efficiency**: As no model training is needed, the chatbot is lightweight and provides fast responses.
- **Flask API**: Handles user queries and returns the best match from the predefined dataset.
- **Easy integration**: Works with a simple web-based UI for users to interact with the bot.
- **Custom dataset**: Works with a CSV file of predefined questions, answers, and associated images.
- **Image support**: Returns both an answer and an associated image (if available) for the best matching query.
- Sample html template included in the repository

![{39FB4FF7-AD7B-4F0B-A79D-1BA39A3480B7}](https://github.com/user-attachments/assets/2da6953d-4fac-4bc7-a490-840c97a5ae52)

![{67157C7B-AF52-4276-8F71-4B04295C6C1F}](https://github.com/user-attachments/assets/77c2f2f7-aa2a-4ff1-b462-1f5fad625e17)

Screenshots from html templates.

## Requirements

- Python 3.x
- Flask
- Flask-CORS
- Scikit-learn
- Pandas
- Numpy

## Setup and Usage

1. Clone the Repository

   ```bash
    git clone https://github.com/SakibAhmedShuva/Simple-QA-ChatBot-Flask-API-No-Training-Required.git
    cd simple-chatbot

2. Install the Required Packages
You can install the required Python packages by running:

   ```bash
    pip install -r requirements.txt

3. Add Your Dataset
Place your questions_answers.csv file in the root directory of the repository. Ensure that it contains at least three columns: Question, Answer, and Image. The Image column can contain filenames of images stored in a static folder.

4. Run the Flask API
Start the Flask server by running the following command:

   ```bash
    python chat-bot.py

The API will be available at http://127.0.0.1:5000.

5. Interact with the Chatbot
Open the chat-bot.html file in your browser to use the chatbot's web interface. You can ask questions and get answers, along with relevant images (if any).

## Example Output:
Sample API Response:
   ```bash
      {
          "query": "What is AI?",
          
          "answer": "AI stands for Artificial Intelligence, which is a branch of computer science.",
          
          "image_url": "http://127.0.0.1:5000/static/ai_image.png"
      }
   ```

**Folder Structure:**
simple-chatbot/
│
├── chat-bot.py               # Flask API for Q&A chatbot
├── chat-bot.html             # Frontend for the chatbot
├── questions_answers.csv      # CSV file containing the questions and answers
├── static/                   # Folder for storing image files
└── requirements.txt           # Required Python packages

Postman API Request Details:
1. API Endpoint (POST Request):

Default URL: http://127.0.0.1:5000/chat-bot  
Method: POST  
Content-Type: application/json  
Request Body (raw/JSON format):

Example body:
```json
{
    "query": "What is AI?"
}
```

2. API Response Example:

Response Status: 200 OK

Response Body (JSON format):

Example response when a matching question is found:
```json
{
    "query": "What is AI?",
    "answer": "AI stands for Artificial Intelligence, which is a branch of computer science.",
    "image_url": "http://127.0.0.1:5000/static/ai_image.png"
}
```

Example response when no matching question is found:
```json
{
    "error": "No query provided"
}
```

3. Error Handling:

If the user query is not provided, the server will respond with:
```json
{
    "error": "No query provided"
}
```
Status Code: 400 Bad Request

