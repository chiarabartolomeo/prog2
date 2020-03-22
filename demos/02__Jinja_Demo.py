from flask import Flask
from flask import render_template
from flask import request

app = Flask("Hello World")

@app.route('/ciao')
def hello_world():
    return render_template('index.html', name="Samir Koce", geschlecht="männlich", geburtsdatum="15.15.2097")

@app.route("/hello5/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Hello " + ziel_person + "!"
        return rueckgabe_string


    return render_template("index.html")


if __name__ == "__main__":
 app.run(debug=True, port=6001)