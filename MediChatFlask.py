from flask import Flask, request, jsonify
import sqlite3
import tensorflow as tf
import nltk

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    answer = get_answer(question)
    save_to_db(question, answer)
    return jsonify({'answer': answer})

def get_answer(question):
    # Use the trained AI model to get the answer
    pass

def save_to_db(question, answer):
    conn = sqlite3.connect('medical_chatbot.db')
    c = conn.cursor()
    c.execute('''INSERT INTO medical_data (question, answer) VALUES (?, ?)''', (question, answer))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run()