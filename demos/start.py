from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask (__name__)
app.secret_key = "abc"
app.permanent_session_lifetime = timedelta(minutes=2)



@app.route('/', methods=["POST", "GET"])
def home():
	if request.method == "POST":
		session.permanent = True
		service = request.form[field1]
		session["service"] = [service]
		name = request.form["field2"]
		session["name"] = name
		phone = request.form["field3"]
		session["phone"] = phone
		message = request.form["field4"]
		session["message"] = message
		date = request.form["field5"]
		session["date"] = date
		time = request.form["field6"]
		session["time"] = time
		return redirect(url_for("home"))
	else: 
		return render_template("home.html") 



if __name__ == "__main__":
 app.run(debug=True)		