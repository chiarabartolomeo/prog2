from flask import Flask, redirect, url_for, render_template, request, session

#Das Wissen haben wir vom Youtube Kanal 'Tech With Tim', unter anderem: https://www.youtube.com/watch?v=mqhxxeeTbu0 

app = Flask (__name__)
app.permanent_session_lifetime = timedelta(minutes=2) #Eingegebene Werte in Session werden 2 Min. lang gespeichert


"""Eingabefeld für den Nutzer. Hier kann der Nutzer Daten zur Dienstleistung, Name, Datum, Uhrzeit etc. eingeben.
Mit der Funktion 'Session' werden die Daten für 2 Min. gespeichert."""
@app.route('/', methods=["POST", "GET"])	
def home():
	if request.method == "POST":			#Die Post Methode dient dazu, die Daten auf den Server zu laden.
		session.permanent = True
		service = request.form["field1"]	#Auswahl Dienstleistung 
		session["service"] = service		#Hier werden die eingegebenen Daten in die Session gespeichert. 
		name = request.form["field2"]		#Dasselbe gilt für die weiteren, folgenden Felder.
		session["name"] = name
		phone = request.form["field3"]
		session["phone"] = phone
		message = request.form["field4"]
		session["message"] = message
		date = request.form["field5"]
		session["date"] = date
		time = request.form["field6"]
		session["time"] = time
		return redirect(url_for("thanks"))	#Nach der Eingabe wird der Nutzer auf die 'Thanks'-Seite weitergeleitet
	else: 
		return render_template("home.html") #Falls die Methode 'GET' ist, wird die Homepage geladen


@app.route('/thanks')	#Erstellun der 'Thanks-Seite'
def thanks():			#Bildung der Funktion 'Thanks'
    date = session["date"]	#Eingegebenes Datum des Kunden wird aufgerufen
    time = session["time"]	#Eingegebene Zeit des Kunden wird aufgerufen
    return render_template("thanks.html", field5 = date, field6 = time) #Der HTML Code wird hier mit den eingegebenen Daten visuel dargestellt.



if __name__ == "__main__":
 app.run(debug=True)		