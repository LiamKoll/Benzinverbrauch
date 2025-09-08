import customtkinter as ctk
import sqlite3
from datetime import datetime

# GUI theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Datenbank Migration: Falls alte Tabelle ohne neue Spalten existiert, erweitern
conn = sqlite3.connect("verbrauchsdaten.db")
c = conn.cursor()

# Prüfen, ob Spalten existieren, ansonsten hinzufügen
c.execute("PRAGMA table_info(verbrauch)")
columns = [info[1] for info in c.fetchall()]

if "euro_pro_liter" not in columns:
    c.execute("ALTER TABLE verbrauch ADD COLUMN euro_pro_liter REAL")
if "kosten_pro_100km" not in columns:
    c.execute("ALTER TABLE verbrauch ADD COLUMN kosten_pro_100km REAL")

conn.commit()
conn.close()


def verbrauch():
    try:
        kilometer = float(kilometerentry.get())
        benzinverbrauch = float(benzinentry.get())
        euro_pro_liter = float(euroentry.get())

        liter_pro_100km = (benzinverbrauch / kilometer) * 100
        kosten_pro_100km = liter_pro_100km * euro_pro_liter

        ergebnislabel.configure(
            text=f"***| Du hast {round(liter_pro_100km, 2)} l/100km verbraucht und daher {round(kosten_pro_100km, 2)} €/100km gezahlt! |***"
        )
    except ValueError:
        ergebnislabel.configure(text="Gebe gültige Nummern ein!")
    except ZeroDivisionError:
        ergebnislabel.configure(text="Du kannst nicht durch 0 teilen!")


def speichern():
    try:
        kilometer = float(kilometerentry.get())
        benzinverbrauch = float(benzinentry.get())
        euro_pro_liter = float(euroentry.get())
        liter_pro_100km = (benzinverbrauch / kilometer) * 100
        kosten_pro_100km = liter_pro_100km * euro_pro_liter
        datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect("verbrauchsdaten.db")
        c = conn.cursor()
        c.execute("""
            INSERT INTO verbrauch (datum, kilometer, benzin, liter_pro_100km, euro_pro_liter, kosten_pro_100km)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (datum, kilometer, benzinverbrauch, liter_pro_100km, euro_pro_liter, kosten_pro_100km))
        conn.commit()
        conn.close()

        ergebnislabel.configure(text="Daten gespeichert!")
    except Exception as e:
        ergebnislabel.configure(text=f"Fehler beim Speichern: {e}")


def zeige_werte():
    fenster = ctk.CTkToplevel(root)
    fenster.title("Gespeicherte Werte")
    fenster.geometry("450x400")
    fenster.iconbitmap("app_icon_hkB_icon.ico")

    def aktualisiere_textfeld():
        textfeld.delete("1.0", "end")
        conn = sqlite3.connect("verbrauchsdaten.db")
        c = conn.cursor()
        c.execute("""
            SELECT id, datum, kilometer, benzin, liter_pro_100km, euro_pro_liter, kosten_pro_100km
            FROM verbrauch ORDER BY id DESC
        """)
        daten = c.fetchall()
        conn.close()

        for eintrag in daten:
            textfeld.insert("end",
                            f"ID: {eintrag[0]}\nDatum: {eintrag[1]}\nKilometer: {eintrag[2]} km\n"
                            f"Benzin: {eintrag[3]} L\nVerbrauch: {round(eintrag[4], 2)} L/100km\n"
                            f"Preis: {round(eintrag[5], 2) if eintrag[5] is not None else '-'} €/L\n"
                            f"Kosten: {round(eintrag[6], 2) if eintrag[6] is not None else '-'} €/100km\n---\n")

    textfeld = ctk.CTkTextbox(fenster, width=420, height=320)
    textfeld.pack(pady=10)

    aktualisiere_textfeld()

    def loesche_letzten():
        conn = sqlite3.connect("verbrauchsdaten.db")
        c = conn.cursor()
        c.execute("DELETE FROM verbrauch WHERE id = (SELECT MAX(id) FROM verbrauch)")
        conn.commit()
        conn.close()
        ergebnislabel.configure(text="Letzter Eintrag gelöscht!")
        aktualisiere_textfeld()

    loeschenbutton = ctk.CTkButton(fenster, text="Letzten Eintrag löschen", command=loesche_letzten, fg_color="red")
    loeschenbutton.pack(pady=5)


def reset():
    benzinentry.delete(0, "end")
    kilometerentry.delete(0, "end")
    euroentry.delete(0, "end")
    ergebnislabel.configure(text="")


# GUI standard
root = ctk.CTk()
root.title("Benzinverbrauch")
root.geometry("500x450")
root.iconbitmap("app_icon_hkB_icon.ico")

# Labels und Felder
kilometerlabel = ctk.CTkLabel(root, text="Wie viel Kilometer bist du gefahren?")
kilometerlabel.pack(pady=12)

kilometerentry = ctk.CTkEntry(root)
kilometerentry.pack()

benzinlabel = ctk.CTkLabel(root, text="Wie viel Benzin hast du verbraucht? (in l)")
benzinlabel.pack(pady=12)

benzinentry = ctk.CTkEntry(root)
benzinentry.pack()

eurolabel = ctk.CTkLabel(root, text="Wie viel Euro hast du pro Liter gezahlt?")
eurolabel.pack(pady=12)

euroentry = ctk.CTkEntry(root)
euroentry.pack()

# Ergebnis label
ergebnislabel = ctk.CTkLabel(root, text="")
ergebnislabel.pack(pady=12)

# Buttons
berechnenbutton = ctk.CTkButton(root, text="Berechnen", command=verbrauch)
berechnenbutton.pack(pady=5)

resetbutton = ctk.CTkButton(root, text="Reset", command=reset, fg_color="red")
resetbutton.pack(pady=5)

wertebutton = ctk.CTkButton(root, text="Vorherige Werte", command=zeige_werte)
wertebutton.pack(pady=5)

speichernbutton = ctk.CTkButton(root, text="Speichern", command=speichern, fg_color="green")
speichernbutton.pack(pady=5)

root.mainloop()
