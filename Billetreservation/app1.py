from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/evenement')
def evenement():
    return render_template('evenement.html')

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')
