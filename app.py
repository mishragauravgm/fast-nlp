from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import time

app = Flask(__name__)

# Load the pre-trained model and tokenizer
model_name = 'distilbert-base-uncased-finetuned-sst-2-english'  # Replace with your model name
tokenizer = AutoTokenizer.from_pretrained(model_name, truncation=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Classification endpoint
@app.route('/classify', methods=['POST'])
def classify():
    start_time = time.time()

    data = request.json
    texts = data.get('texts', [])

    results = []

    for text in texts:
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = logits.argmax().item()

        results.append({'text': text, 'predicted_class': predicted_class})

    end_time = time.time()
    total_time = end_time - start_time

    return jsonify({'results': results, 'total_time_taken': total_time})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)