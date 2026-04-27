# ⛽ Benzinverbrauch Tracker

[Beitrag zum Projekt: Benzinverbrauch App](https://liamkollaczek.vercel.app/projekte/benzin)

Eine einfache und praktische Desktop-Anwendung, um den Benzinverbrauch pro 100 km sowie die Kosten pro 100 km zu speichern und im Blick zu behalten. 

Ursprünglich entstanden aus dem Bedarf, für ein älteres Auto (wie z. B. einen Opel Corsa B aus dem Jahr 1996) ohne modernen Bordcomputer den Verbrauch, die Spritkosten und die Effizienz der eigenen Fahrweise zu tracken.

## 🎥 Programm-Review & Showcase

Möchtest du sehen, wie das Programm funktioniert? Schau dir hier die kurze Review dazu an:

<a href="https://www.youtube.com/watch?v=whxZWInA4x8">
  <img src="https://github.com/user-attachments/assets/9f0aacab-5e80-42e3-801e-ec23546edd24" alt="Tankanzeige" width="900" height="400" />
</a>
<br>
<em>*(Klicke auf das Bild, um das Video auf YouTube anzusehen)*</em>

---

## ✨ Funktionen

- **Einfache Berechnung:** Gib einfach die gefahrenen Kilometer, die getankten Liter und den Preis pro Liter ein.
- **Sofort-Auswertung:** Das Programm berechnet automatisch deinen Durchschnittsverbrauch auf 100 km und die entsprechenden Kosten in €.
- **Verlauf und Historie:** Dank der integrierten Datenbank werden alle deine Tankvorgänge mit Datum gespeichert. Unter dem Bereich "Vorherige Werte" kannst du perfekt nachverfolgen, wie viel du in den letzten Monaten ausgegeben hast und ob du effizient unterwegs warst.

---

### 🛠️ Schnellstart: So öffnest du das Programm

Du brauchst keine Programmierkenntnisse oder zusätzliches Setup, um den Tracker zu nutzen. Folge einfach diesen Schritten:

1. **📥 Herunterladen:**
   Klicke auf der GitHub-Seite oben rechts auf den grünen Button **`<> Code`** und wähle **`Download ZIP`**.
2. **🗂️ Entpacken:**
   Entpacke den heruntergeladenen ZIP-Ordner an einem Ort deiner Wahl auf deinem Computer.
3. **🔍 Datei finden:**
   Öffne den entpackten Ordner und navigiere zum Unterordner `dist`. Dort findest du die Anwendungsdatei namens **`main.exe`**.
4. **🚀 Starten:**
   Öffne die **`main.exe`** mit einem einfachen Doppelklick.

> **🎉 Fertig!** Das Programm öffnet sich sofort und du kannst direkt anfangen, deine ersten Werte einzutragen. Eine Installation ist nicht erforderlich!

---

## 💻 Für Entwickler (Technologien)

Wenn du dir den Code ansehen oder ihn erweitern möchtest, kannst du natürlich auch direkt die Python-Datei nutzen:

- **Programmiersprache:** Python (`main.py`)
- **Datenbank:** SQLite (`verbrauchsdaten.db`) – Für die lokale, leichtgewichtige und offline-verfügbare Speicherung deiner Daten.
- **Build-Tool:** PyInstaller (`main.spec`) – Um den Code in eine ausführbare `.exe` umzuwandeln. 

Lies dir gerne die vollständige Entstehungsgeschichte des Projekts, warum der Verbrauch so wichtig ist und weitere Gedanken dazu auf meiner Portfolio-Website durch:
👉 [Beitrag zum Projekt: Benzinverbrauch App](https://liamkollaczek.vercel.app/projekte/benzin)
