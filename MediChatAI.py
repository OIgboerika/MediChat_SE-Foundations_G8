import tensorflow as tf
import nltk

# Load medical databases and pre-trained AI models

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")
    if filter_non_medical_questions(question):
        medical_answer = generate_medical_answer(question)
        return jsonify({"status": "success", "answer": medical_answer})
    return jsonify({"status": "error", "message": "Question not related to medical field"})

def filter_non_medical_questions(question):
    # Filter out non-medical questions using NLP techniques
    pass

def generate_medical_answer(question):
    # Generate medical answers using AI models
    pass