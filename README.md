
﻿<h1>Projektidee:</h1> 
Reservierungstool für Coiffeuretermine. Unser Ziel ist es, ein Tool zu programmieren, wo Kunden sich selbständig einen Termin per Klick bei ihrem Coiffeur reservieren können.

Als erstes wird der Kunde nach seiner gewünschten Behandlung gefragt, also ob dieser nur die Haare schneiden lassen möchte, ob nur der Bart gemacht werden soll oder beides. Der Kunde kann dann seine persönlichen Daten eingeben und seinen Wunsch-Termin per Kalenderklick (Chromebrowser) eingeben. Anschliessend wird dem Kunden eine Bestätigsseite angezeigt, wo ersichtlich ist, dass seine Reservation funktioniert hat und der reservierte Termin angezeigt wird.

<h2>Installation:</h2>
1) Öffnen Sie das Terminal.
2) Navigieren Sie in den heruntergeladenen Ordner "prog2" mit dem Kommando "cd".
3) Navigieren Sie in den Ordner "demos" mit cd.
4) Geben Sie folgendes in das Terminal ein: python start.py
5) Kopieren Sie den angezeigten Link und fügen Sie diesen in ihrem Browser (Vorzugsweise Chrome) ein.

<h2>Bedienung:</h2>
1) Geben Sie Ihre persönlichen Daten ein.
2) Klicken Sie auf den Button "Senden"
3) Geben Sie, unter den vorgegebenen Bedingungen, ihr Wunschdatum und die Uhrzeit ein.
4) Klicken Sie auf den Button "Senden".
5) Ihre Kontaktdaten, sowie die Terminbestätigung werden nun angezeigt. 

*Falls Sie einen belegten Termin, oder ein Datum eingegeben haben welches nicht zur Verfügung steht, haben Sie die Möglichkeit eine weitere Termineingabe zu machen. 


<h2>Funktionsweise:</h2>
Die Daten werden mit HTML-Tag "Input" vom Nutzer abgeholt, anschliessend in eine Session zwischengespeichert. Die Termine werden dauerhaft in eine JSON-Datei abgespeichert. Diverese Umwandlungen wurden für Berechnungen und Vergleiche vorgenommen.


<h2>Zusatz:</h2>
-Unsere erstellte Seite besteht aus den Grund-Seiten "Home = /", "Thanks = /thanks/", "Termine = /termine/" 

