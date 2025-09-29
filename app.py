from flask import Flask, render_template, request, jsonify
import json
from difflib import SequenceMatcher

app = Flask(__name__)

def load_responses():
    with open('data/responses.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def find_best_match(user_question, intents):
    best_match = None
    highest_ratio = 0
    
    for intent in intents:
        for pattern in intent['patterns']:
            similarity = SequenceMatcher(None, user_question.lower(), pattern.lower()).ratio()
            if similarity > highest_ratio:
                highest_ratio = similarity
                best_match = intent
    
    # Seuil de similarité de 0.6 (60%)
    if highest_ratio > 0.6:
        # Retourne une réponse aléatoire parmi les réponses disponibles
        import random
        return random.choice(best_match['responses'])
    return "Désolé, je ne comprends pas votre question. Pouvez-vous la reformuler ?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json['question']
    responses = load_responses()
    answer = find_best_match(user_question, responses['questions'])
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True) 