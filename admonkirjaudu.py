"""
Malaz Bittar

"""


def main():
    
import tkinter as tk
import sqlite3

def authenticate():
	email_or_phone = email_or_phone_entry.get()
	password = password_entry.get()

	conn = sqlite3.connect('tietokanta.db')
	c = conn.cursor()

	c.execute("SELECT * FROM users WHERE email_or_phone=? AND password=?", (email_or_phone, password))
	result = c.fetchone()

	if result:
	welcome_label.config(text="Tervetuloa, " + result[1] + "!")
	else:
	welcome_label.config(text="Virheellinen sähköpostiosoite/puhelinnumero tai salasana. Yritä uudelleen.")

	email_or_phone_entry.delete(0, tk.END)
	password_entry.delete(0, tk.END)

	window = tk.Tk()

	email_or_phone_label = tk.Label(window, text="Järjestelmänvalvojan sähköpostiosoite tai puhelinnumero")
	email_or_phone_label.pack()

	email_or_phone_entry = tk.Entry(window)
	email_or_phone_entry.pack()

	password_label = tk.Label(window, text="Pythonin salasana")
	password_label.pack()

	password_entry = tk.Entry(window, show="*")
	password_entry.pack()

	authenticate_button = tk.Button(window, text="Tunnistaudu", command=authenticate)
	authenticate_button.pack()

	welcome_label = tk.Label(window, text="")
	welcome_label.pack()

	window.mainloop()

if __name__ == "__main__":
    main()
