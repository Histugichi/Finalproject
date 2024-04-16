from flask import Flask, render_template, request, session, url_for, redirect
#from flask_bcrypt import Bcrypt
from base64 import decode
import bcrypt


from users.user_dao import UserDao
from users.user import User
from evenements.evenement import Evenement
from evenements.evenement_dao import EvenementDao
from paiements.paiement import Paiement
from paiements.paiement_dao import PaiementDao
from reservations.reservation_dao import ReservationDao
from reservations.reservation import Reservation


app = Flask(__name__,)
app.secret_key = 'secretkey'
#bcrypt = Bcrypt(app)
salt = bcrypt.gensalt(rounds=15)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods= ['POST', 'GET'])
def login():
    req = request.form
    message =None
    user = None

    if request.method == "POST":
        username = req ['username']
        password = req ['password']     
        password = password.encode('utf-8')
        if username=="" or password=="":
            message="error"
        else:
            # Chercher hashed password de la base de donnée base sur username
            message,user= UserDao.get_one(username)
            hashed_password_bd = user[2]
          
            if hashed_password_bd:
                 hashed_password_bd = hashed_password_bd.encode('utf-8')
                # Verifier si le mot de passe est correct
            if bcrypt.checkpw(hashed_password_bd,password):
                    message = 'success'
                   
                    if user:
                        session['nom_complet']=user[0] #On met le nom complet dans notre variable de session
                        session['username']=user[1] # On met le username dans notre variable de session
                        return redirect(url_for("home"))   
            
        message= 'Username et password invalide'
    return render_template('login.html', message=message, user=None)

@app.route('/registrer',methods= ['POST', 'GET'])
def registrer():
    req = request.form
    message =None
    user= None

    if request.method == "POST":
        nom_complet = req ['nom_complet']
        username = req ['username']
        password = req ['password']
        #Hash password
        is_admin= 0
        password = password.encode('utf-8')
        
        hashed_password = bcrypt.hashpw(password, salt)
        
        if nom_complet=="" or username=="" or password=="" :
            message="error"
        else:
            user = User(nom_complet, username, hashed_password, is_admin)
            message = UserDao.create(user)
        print(message)
    return render_template('registrer.html', message=message, user=user)

@app.route('/evenement')
def evenement():
    return render_template('evenement.html')

@app.route("/logout")
def logout():
    session.clear() # On vide la session
    return redirect(url_for('login'))



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

@app.route("/users")
def users():
    if 'username' not in session:
        return redirect(url_for('login'))
    message, users = UserDao.list_all()
    return render_template("liste_users.html", message= message, users= users)

@app.route('/add-users', methods= ['POST', 'GET'])
def add_user():
    if 'username' not in session:
        return redirect(url_for('login'))
    req = request.form
    message =None
    user= None

    if request.method == "POST":
        nom_complet = req ['nom_complet']
        username = req ['username']
        password = req ['password']
        type = req ['type']
        
        if nom_complet=="" or username=="" or password=="" or type=="":
            message="error"
        else:
            user = User(nom_complet,username,password, type)
            message = UserDao.create(user)
        print(message)
    return render_template('add_users.html', message= message, user=user)

@app.route('/paiement', methods=['POST','GET'])
def paiement():
    if request.method == 'POST':
        card_number = request.form['card_number']
        expiry_date = request.form['expiry_date']
        cvv = request.form['cvv']
    return render_template('paiement.html')
    

    
if __name__ == "__main__":
    app.run(debug=True)
