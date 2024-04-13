from flask import Flask, render_template

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

@app.route('/paiement')
def paiement():
    return render_template('paiement.html')

if __name__ == "__main__":
    app.run(debug=True)
