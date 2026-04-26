# ⛽ Benzinverbrauch Tracker

[Beitrag zum Projekt: Benzinverbrauch App](https://liamkollaczek.vercel.app/projekte/benzin)

Eine einfache und praktische Desktop-Anwendung, um den Benzinverbrauch pro 100 km sowie die Kosten pro 100 km zu speichern und im Blick zu behalten. 

Ursprünglich entstanden aus dem Bedarf, für ein älteres Auto (wie z. B. einen Opel Corsa B aus dem Jahr 1996) ohne modernen Bordcomputer den Verbrauch, die Spritkosten und die Effizienz der eigenen Fahrweise zu tracken.

## ✨ Funktionen

- **Einfache Berechnung:** Gib einfach die gefahrenen Kilometer, die getankten Liter und den Preis pro Liter ein.
- **Sofort-Auswertung:** Das Programm berechnet automatisch deinen Durchschnittsverbrauch auf 100 km und die entsprechenden Kosten in €.
- **Verlauf und Historie:** Dank der integrierten Datenbank werden alle deine Tankvorgänge mit Datum gespeichert. Unter dem Bereich "Vorherige Werte" kannst du perfekt nachverfolgen, wie viel du in den letzten Monaten ausgegeben hast und ob du effizient unterwegs warst.

## 🚀 Ausführung als .exe (Sehr einfach!)

Du musst kein Programmierer sein oder Python installiert haben, um dieses Tool zu nutzen! Das Programm wurde als ausführbare Datei verpackt, sodass es unter Windows sofort einsatzbereit ist.

1. Lade dir die Dateien des Projekts herunter (z.B. über den grünen "Code" Button -> "Download ZIP").
2. Entpacke den Ordner.
3. Suche nach der Anwendungsdatei (in der Regel im Ordner `dist` oder als direkter Download bereitgestellt) mit dem Namen **`main.exe`**.
4. Öffne die `.exe`-Datei per Doppelklick.
5. Das Programm startet sofort und du kannst anfangen, deine Werte einzutragen!

## 💻 Für Entwickler (Technologien)

Wenn du dir den Code ansehen oder ihn erweitern möchtest, kannst du natürlich auch direkt die Python-Datei nutzen:

- **Programmiersprache:** Python (`main.py`)
- **Datenbank:** SQLite (`verbrauchsdaten.db`) – Für die lokale, leichtgewichtige und offline-verfügbare Speicherung deiner Daten.
- **Build-Tool:** PyInstaller (`main.spec`) – Um den Code in eine ausführbare `.exe` umzuwandeln.

## 👨‍💻 Autor & Hintergrundstory

Entwickelt von **Liam Kollaczek**. 

Lies dir gerne die vollständige Entstehungsgeschichte des Projekts, warum der Verbrauch so wichtig ist und weitere Gedanken dazu auf meiner Portfolio-Website durch:
👉 [Beitrag zum Projekt: Benzinverbrauch App](https://liamkollaczek.vercel.app/projekte/benzin)
