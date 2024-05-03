from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

context_data = ""

@app.before_first_request
def load_context():
    global context_data
    with open('contexts.txt', 'r') as file:
        context_data = file.read()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-answer', methods=['POST'])
def fetch_answer():
    question = request.json['question']
    

    api_url = 'https://api-inference.huggingface.co/models/AlexYang33/bert-finetuned-sql'
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "inputs": {
            "question": question,
            "context": context_data
        }
    }

    response = requests.post(api_url, headers=headers, json=data)
    answer = response.json()['answer']
    print(answer)
    return jsonify(answer=answer)


if __name__ == '__main__':
    app.run(debug=True)
