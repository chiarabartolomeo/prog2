from flask import Flask
from flask import render_template
from flask import request

app = Flask("Hello World")

@app.route('/hello')
def hello_world():
    return render_template('index.html', name="Samir Koce", geschlecht="männlich", geburtsdatum="15.15.2097")


if __name__ == "__main__":
	app.run(debug=True, port=5000)