from flask import Flask, render_template, request, session, url_for, redirect


app = Flask(__name__)
app.secret_key='secretkey'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/evenement')
def evenement():
    return render_template('evenement.html')


@app.route('/paiement')
def paiement():
    return render_template('paiement.html')
