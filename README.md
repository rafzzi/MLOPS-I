# MLOps-I
Machine Larning Operations Project I:
Developing two different models and deploying them with an API using Flask.

## main.py
The main structure of the API:
- loads the models built on the jupyter notebooks with pickle
- declare the routes to the endpoints containing each functionality
- contains a basic authentication to prevent unwanted access.

## analise_de_sentimento.ipynb
Jupyter Notebook containing a simple model from TextBlob to 
analyse the sentiment of a sentence (in pt-br).

## house_pricing.ipynb
Jupyter Notebook containing a link to a github csv, using this
data to create a linear regression with sklearn to predict 
house pricing from data of size, year and garage.
This model is dumped as 'lr.pkl' to be used on the API app, 
the scaler used on the data is also dumped as 'scaler.pkl'.

## requests.ipynb
Jupyter Notebook to test requests and authentication of the flask app.

## requirements.txt
to run the app simply download and unzip the file, then open terminal (bash or zsh) and run:

<code>
python3 -m venv venv
</code>
<br><br><code>
source venv/bin/activate
</code>
<br><br><code>
pip install -r requirements.txt
</code>
<br><br><code>
python3 main.py
</code>
