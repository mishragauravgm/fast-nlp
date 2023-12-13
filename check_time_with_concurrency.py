import csv
import requests
import time
import concurrent.futures
import json

# Flask app URL
flask_app_url = 'http://localhost:5005/classify'  # The URL on which flask is running

# Read text from CSV file
texts = []
with open('IMDB Dataset.csv', 'r') as file: #reading the dataset
    reader = csv.DictReader(file)
    for i,row in enumerate(reader):
        texts.append(row['review'])
        if(i==1000): #it was taking longer to check for all 50000 entries hence checking on 10005 entries
            break;
# Function to classify text
def classify_text(text):
    payload = {'texts': [text]}
    #print(payload)
    response = requests.post(flask_app_url, json=payload)
    #print(response)
    if response.status_code == 200:
        result = response.json()['results']#[0]
        print(result['predicted_class'])
        return result
    else:
        return {'text': text, 'predicted_class': 'Error'}

# Measure time taken for concurrent requests
start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    results = list(executor.map(classify_text, texts)) #Sending concurrent requests
end_time = time.time()
total_time = end_time - start_time

print(f"Processing completed in {total_time} seconds for {len(results)} entries with acceleration.")

with open("with_concurrency.json", "w") as outfile:
    json.dump(results, outfile)
#print(results)


