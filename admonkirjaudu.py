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
window.title("ML")
window.geometry("500x300")
window.configure(background='black')  # asettaa taustavärin mustaksi

welcome_label = tk.Label(window, text="Admin kirjaudu", bg="black", fg="white", font=("Helvetica", 16))
welcome_label.place(relx=0.5, rely=0.1, anchor="center")   

email_or_phone_label = tk.Label(window, text="Anna sähköpostiosoite tai puhelinnumero", bg="black", fg="white", font=("Helvetica", 14))
email_or_phone_label.place(relx=0.5, rely=0.3, anchor="center")

email_or_phone_entry = tk.Entry(window)
email_or_phone_entry.place(relx=0.5, rely=0.4, anchor="center")

password_label = tk.Label(window, text="Anna salasana", bg="black", fg="white", font=("Helvetica", 14))
password_label.place(relx=0.5, rely=0.5, anchor="center")

password_entry = tk.Entry(window, show="*")
password_entry.place(relx=0.5, rely=0.6, anchor="center")

authenticate_button = tk.Button(window, text="Jatka", command=authenticate)
authenticate_button.place(relx=0.5, rely=0.8, anchor="center")

#welcome_label = tk.Label(window, text="Jatka", bg="black", fg="white", font=("Helvetica", 16))
#welcome_label.place(relx=0.5, rely=0.8, anchor="center")

window.mainloop()
    
