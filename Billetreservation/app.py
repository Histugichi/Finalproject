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

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/evenement')
def evenement():
    return render_template('evenement.html')

@app.route('/reservations', methods=['POST'])
def reservations():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.form['nom']
        email = request.form['email']
        date = request.form['date']
        # Ici, vous pouvez traiter les données de réservation, comme les enregistrer dans une base de données, etc.
        return render_template('confirmation.html', nom=nom, email=email, date=date)

@app.route('/')
def paiement():
    return render_template('paiement.html')

@app.route('/process_paiement', methods=['POST'])
def process_paiement():
    if request.method == 'POST':
        card_number = request.form['card_number']
        expiry_date = request.form['expiry_date']
        cvv = request.form['cvv']
        # Traiter les données du formulaire de paiement ici
        # Par exemple, enregistrer les détails de paiement dans une base de données ou les transmettre à un service de paiement tiers
        return "Paiement reçu avec succès!"
    

    
if __name__ == "__main__":
    app.run(debug=True)
