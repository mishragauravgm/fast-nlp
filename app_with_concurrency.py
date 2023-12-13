from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import concurrent.futures
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

app = Flask(__name__)

# Load the Hugging Face model and tokenizer
model_name = 'aigurugaurav/sentiment_detection'  # Replace with your model name
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForSequenceClassification.from_pretrained(model_name)
#results = []
# Function to perform text classification
def classify_text(text):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    inputs = tokenizer(text, return_tensors="pt",truncation=True)
    outputs = model(**inputs)
    predicted_class = outputs.logits.argmax().item()
    return {'text': text, 'predicted_class': predicted_class}

# Concurrent request handling endpoint
@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    texts = data.get('texts', [])
    #with concurrent.futures.ThreadPoolExecutor() as executor: #executing concurrent requests
    #    results = list(executor.map(classify_text, texts))
    #results.append(classify(texts['text']))
    results = classify_text(texts)
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)