from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob

import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

lr = pickle.load(open('lr.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

colunas = ['tamanho', 'ano', 'garagem']

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'raf'
app.config['BASIC_AUTH_PASSWORD'] = 'figa'

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return '<h1>Minha primeira API</h1>'

@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(from_lang='pt-br', to='en')
    polaridade = tb_en.sentiment.polarity
    return f'Polaridade: {polaridade}'

@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    predicao = lr.predict(scaler.transform([dados_input]))
    return jsonify(preco=predicao[0])

app.run(debug=True) 