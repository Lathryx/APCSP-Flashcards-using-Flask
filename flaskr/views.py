from flaskr import app
from flask import redirect, url_for, render_template

# home page
@app.route('/')
def home():
    return render_template('home.html')

# flashcard page
@app.route('/flashcard')
def flashcard_home():
    return redirect(url_for('flashcard_home')+'/0')
@app.route('/flashcard/<number>')
def flashcard(number=None, total=56):
    return render_template('flashcard.html', number=str(int(number)+1), total=total)

# declare route for JSON file to get data 
@app.route('/flashcard/apcsp_defs.json')
def defs():
    return render_template('apcsp_defs.json')