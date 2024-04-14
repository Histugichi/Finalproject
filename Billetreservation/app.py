from flask import Flask, render_template, request, session, url_for, redirect
from voyageur.utilisateur import User
from voyageur.utilisateur_dao import Userdao

app = Flask(__name__, static_folder='C:/Users/maxle/OneDrive/Bureau/python/tp/ProjetFinal/static')
app.secret_key = 'secretkey'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/evenement')
def evenement():
    return render_template('evenement.html')

@app.route('/reservations', methods=['POST', 'GET'])
def reservations():
    nom=None
    email=None
    date=None
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        date = request.form['date']
    return render_template('reservations.html', nom=nom, email=email, date=date)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/paiement', methods=['POST','GET'])
def paiement():
    if request.method == 'POST':
        card_number = request.form['card_number']
        expiry_date = request.form['expiry_date']
        cvv = request.form['cvv']
    return render_template('paiement.html')
    

    
if __name__ == "__main__":
    app.run(debug=True)
