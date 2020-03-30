from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

app = Flask("Hello World")

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route("/anmelden/", methods=['GET', 'POST'])
def anmelden():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        return redirect(url_for("angebote", name=ziel_person))


    return render_template("anmelden.html")

@app.route("/angebote/<name>", methods=['GET'])
def angebote(name):
	return render_template("angebot.html", name=name)


if __name__ == "__main__":
 app.run(debug=True, port=5000)