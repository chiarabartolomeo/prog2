from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
from datetime import datetime, timedelta
from json import loads, dumps

#Das Wissen haben wir vom Youtube Kanal 'Tech With Tim', unter anderem: https://www.youtube.com/watch?v=mqhxxeeTbu0 

app = Flask (__name__)
app.secret_key = "abc"
app.permanent_session_lifetime = timedelta(minutes=2) #Eingegebene Werte in Session werden 2 Min. lang gespeichert


"""Eingabefeld für den Nutzer. Hier kann der Nutzer Daten zur Dienstleistung, Name, Datum, Uhrzeit etc. eingeben.
Mit der Funktion 'Session' werden die Daten für 2 Min. gespeichert."""
#app.route definiert den Link in diesem Fall die html-Seite "Home"
@app.route('/', methods=["POST", "GET"])	
def home():									#Alles was folgt, gehört zur home.html Seite (Definition)

											#POST-Methode wird angewandt, wenn auf den "senden-button" geklickt wird
    if request.method == "POST":			#Wenn Post-Methode verwendet wird, wird alles was eingerückt ist ausgeführt. 
        session.permanent = True
        service = request.form["field1"]	#Auswahl Dienstleistung 
        session["service"] = service		#Hier werden die eingegebenen Daten in die Session gespeichert. 
        if "service" in session:			#Diese if-Abfragen sind nötig, da der Inhalt ansonsten nur aus Zahlen bestehen würde.
            service = session["service"]
            if service == "1":      
                service = "Haare" 
            elif service == "2":
                service = "Bart"
            elif service == "3":
                service = "Haare & Bart" 

        if service == "Haare":				#Hier werden die Kosten für die Leistungen definiert.
            kosten = int(24)				#Haarschnitt kostet 24
        elif service == "Bart":
            kosten = int(15) 				#Bart kostet 15
        else:
            kosten = int(32) 				#Haare und Bart kostet 32
        session["kosten"] = kosten

        name = request.form["field2"]		#Hier werden die Eingaben des Nutzers in die Session gespeichert (für 2 Min) 
        session["name"] = name
        phone = request.form["field3"]
        session["phone"] = phone
        alter = request.form["field4"]
        session["alter"] = alter
        return redirect(url_for("termin"))	#Nach der Eingabe wird der Nutzer auf die "Termin"-Seite weitergeleitet

    return render_template("home.html")		#Bedeuted, dass mit Eingabe "/" im Browser auf Seite "home" verwiesen wird

@app.route('/termin/', methods=["POST", "GET"])    
def termin():
# Daten einlesen
    with open('reservierungen.json') as open_file:	#Hier wird das json-File mit den reservierten Daten geöffnet und als open_file benannt
        json_als_string = open_file.read()			#Das geöffnete json-File wird gelesen und in Variabel json_als_string gespeichert
        reservierungen = loads(json_als_string)		#Die Daten werden geladen und in Variabel reservierungen gespeichert

    if request.method == "POST":            #Die Post Methode dient dazu, die Daten auf den Server zu laden.
        session.permanent = True
        date = request.form["field5"]
        session["date"] = date
        return redirect(url_for("thanks"))  #Nach der Eingabe wird der Nutzer auf die 'Thanks'-Seite weitergeleitet

    

    
    return render_template("termin.html", reservierungen=reservierungen)

  

@app.route('/thanks', methods=["POST", "GET"])	#Erstellung der 'Thanks-Seite'
def thanks():			#Bildung der Funktion 'Thanks'
    # Daten einlesen json laden
    with open('reservierungen.json') as open_file:	#Hier wird das json-File mit den reservierten Daten geöffnet und als open_file benannt
        json_als_string = open_file.read()			#Das geöffnete json-File wird gelesen und in Variabel json_als_string gespeichert
        reservierungen = loads(json_als_string)		#Die Daten werden geladen und in Variabel reservierungen gespeichert

    if request.method == "POST":            #Die Post Methode dient dazu, die Daten auf den Server zu laden.
        session.permanent = True
        date = request.form["field5"]    #Auswahl Dienstleistung 
        session["date"] = date        #Hier werden die eingegebenen Daten in die Session gespeichert. 
    
    if "service" in session:			#Umwandlung Dienstleistungsauswahl von Session in Service 
        service = session["service"]
        if service == "1":
            service = "Haare"
        elif service == "2":
            service = "Bart"
        elif service == "3":
            service = "Haare & Bart"
    name = session["name"]
    phone = session["phone"]
    kosten = session["kosten"]
    alter = session["alter"]
    alter = int(alter)
    if alter < 18:
        kosten = kosten - 4 #wenn unter 18 rabatt von 4 CHF
    date = session["date"]
    print(date)	#Eingegebenes Datum des Kunden wird aufgerufen
    umwandeln = datetime.strptime( date, "%Y-%m-%dT%H:%M" ) #umwandeln in datetime format
    #Quelle: https://www.programiz.com/python-programming/datetime/strftime, https://www.programiz.com/python-programming/datetime/strptime
    date_formatiert = umwandeln.strftime("%d.%m.%Y-%H:%M") #umwandeln in ein string
    umwandeln_2 = datetime.strptime( date_formatiert, "%d.%m.%Y-%H:%M") #umwandeln in datetime format
    print(date_formatiert)
    reservierung_existiert_bereits = False
    for reservierung in reservierungen:
        if reservierung == date_formatiert:
            reservierung_existiert_bereits = True

    date_ohne_zeit = umwandeln.strftime("%d.%m.%Y")
    wochentag = umwandeln.strftime("%A")
    zeiten = {"09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30"}
    zeit = date[11:]
    today = datetime.today()
    now = today.strftime("%Y-%m-%dT%H:%M")

    if date < now:
        return render_template("vergangen.html", Reservierung=date_ohne_zeit)
    elif wochentag == "Sunday":
        return render_template("sonntag.html", Reservierung=date_ohne_zeit)
    elif zeit not in zeiten:
        return render_template("zeit.html", zeit=zeit)
    elif reservierung_existiert_bereits == True: #Falls ein Termin bereits vergeben wurde
        nächst_mögl_termin = umwandeln_2 + timedelta(minutes=30) #umwandeln in datetime um zu addieren
        reservierung_existiert_bereits = True
        while reservierung_existiert_bereits == True:
            nächst_mögl_termin_1 = nächst_mögl_termin.strftime("%d.%m.%Y-%H:%M")#umwandeln in ein string
            if nächst_mögl_termin_1[11:] == "19:00":
                umwandeln_2 = datetime.strptime(nächst_mögl_termin_1, "%d.%m.%Y-%H:%M")
                nächst_mögl_termin = umwandeln_2 + timedelta(hours=14) #umwandeln in datetime um zu addieren
                wochentag_2 = nächst_mögl_termin.strftime("%A") #umwandeln in wochentag
                if wochentag_2 == "Sunday":
                    nächst_mögl_termin = umwandeln_2 + timedelta(days=1) #umwandeln in datetime um zu addieren
                
                
            else:
                if nächst_mögl_termin_1 in reservierungen:
                    reservierung_existiert_bereits = True
                else:
                    reservierung_existiert_bereits = False
                umwandeln_2 = datetime.strptime( nächst_mögl_termin_1, "%d.%m.%Y-%H:%M" )
                nächst_mögl_termin = umwandeln_2 + timedelta(minutes=30) #umwandeln in datetime um zu addieren
        
        return render_template("reserviert.html", reserviert=date_formatiert, reservierungen=reservierungen, alternative=nächst_mögl_termin_1)

    else:
        reservierungen.append(date_formatiert)
        # Daten speichern
        with open('reservierungen.json', 'w') as open_file:
            json_als_string = dumps(reservierungen)
            open_file.write(json_als_string)
        return render_template("thanks.html", Datum=date_ohne_zeit, Zeit=zeit, name=name, alter=alter, kosten=kosten, service=service, phone=phone)






if __name__ == "__main__":
 app.run(debug=True)		