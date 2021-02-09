#! /usr/bin/python3
from flask import Flask, Response, render_template, request, session

app = Flask(__name__, static_url_path="/static")

app.secret_key = b'appli de test'
@app.route("/")
def mainpage():
  game = {}
  if 'user' in session:
    game.update({'user': session['user']})
  return render_template("index.html", game=game)


def hg_hide(mot, lettre):
    ret = ""
    manquant = 0
    for i in mot:
        if i in lettre:
            ret += i + " "
        else:
            manquant += 1
            ret += "_ "
    if manquant == 0:
        session['win'] = 1
        session.modified = True
    return ret

@app.route("/game", methods=['POST', 'GET'])
def game():
    game = {}
    if request.method == 'POST':
        print(session)
        if not 'user' in session:
            if 'user' in request.form:
                session['win'] = 0
                session['user'] = request.form['user']
                session['status'] = 0
                session['lettre'] = []
                with open('/opt/base/country.txt') as c:
                    country = c.readlines()
                    from random import randint
                    nb = randint(0, len(country))
                    session['mot'] = country[nb].upper().strip()
                print('new user')
        else:
            if 'lettre' in request.form:
                l_lettre = request.form['lettre'].upper()
                if l_lettre in session['lettre']:
                    game.update({'error': "lettre déja proposée"})
                else:
                    session['lettre'].append(l_lettre)
                    if not l_lettre in session['mot']:
                        session['status'] += 1
                    print(session['lettre'])
            if 'user' in request.form:
                game.update({"error": "utilisateur déjà connecté"})
    game.update({'status': session['status'],
                 'user': session['user'],
                 'try': session['lettre'],
                 'mot': hg_hide(session['mot'], session['lettre'])})
    session.modified = True
    if session['status'] >= 6:
        game.update({'mot': session['mot']})
    if session['win'] == 1:
        game.update({'win': True})
    return render_template("game.html", game=game)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('user')
    return render_template("login.html")

@app.errorhandler(404)
def not_found(err):
    return render_template('404.html', path=request.path), 404

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000, debug=True)
