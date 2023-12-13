import csv
import requests
import time
import json

# Flask app URL
flask_app_url = 'http://localhost:5001/classify'  # Flask app URL without any concurrency settings


# Function to classify text
def classify_text(text):
    payload = {'texts': [text]} #preparing the payload
    #print(payload)
    response = requests.post(flask_app_url, json=payload) #getting response from the Flask App
    #print(response)
    if response.status_code == 200: 
        result = response.json()['results'][0]
        #print(result['predicted_class'])
        return result
    else:
        return {'text': text, 'predicted_class': 'Error'}
# Read text from CSV file
results = []

start_time = time.time()
with open('IMDB Dataset.csv', 'r') as file:
    reader = csv.DictReader(file)
    for i,row in enumerate(reader):
        #texts.append(row['review'])
        results.append(classify_text(row['review']))
        if(i==1000):
            break;

end_time = time.time()
total_time = end_time - start_time
#print(results)
with open("without_concurrency.json", "w") as outfile:
    json.dump(results, outfile)

#print(results)
print(f"Processing completed in {total_time} seconds for {len(results)} entries without acceleration.")