# Accelerating inference using Multi-threading

**Here are the results for 1000 samples(the model with F1 score of 0.907 was chosen:**


> with_concurrency = 89.19 seconds
> without_concurrency = 137.64 seconds
Speed-up Factor = ~1.5 times

Install the requirements by using pip(assuming you already have python 3.10 installed)
>pip install -r requirements.txt

#### To run the simple flask app without concurrency:
>python app.py
>python check_time.py

#### To run the Flask app with concurrency:
>gunicorn -b 0.0.0.0:5005 -w 8 app_with_concurrency:app
>python check_time_with_concurrency.py

*This will print the output with time and number of samples processed. Note that by default it only processes first 1000 entries from the IMDB dataset*

To view results from terminal and colab, you can view them in results folder.
