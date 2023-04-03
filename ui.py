import tkinter as tk

def asiakas_valinta():
    print("Valitsit Asiakas")

def admin_valinta():
    print("Valitsit Admin")
def main():
	ikkuna = tk.Tk()
	ikkuna.title("ML")

	ikkuna.geometry("500x300")
	ikkuna.configure(background='black')  # asettaa taustavärin mustaksi
	Ml_label = tk.Label(ikkuna, text="Tervetuloa ML verkkokauppa?", bg="black", fg="white", font=("Helvetica", 16))
	Ml_label.place(relx=0.5, rely=0.1, anchor="center")

	kysymys_label = tk.Label(ikkuna, text="Oletko?", bg="black", fg="white", font=("Helvetica", 16))
	kysymys_label.place(relx=0.5, rely=0.3, anchor="center")  # keskittää kysymyslabelin

	asiakas_button = tk.Button(ikkuna, text="Asiakas", command=asiakas_valinta)
	asiakas_button.place(relx=0.4, rely=0.5, anchor="center")

	admin_button = tk.Button(ikkuna, text="Admin", command=admin_valinta)
	admin_button.place(relx=0.6, rely=0.5, anchor="center")

	ikkuna.mainloop()
if __name__ == "__main__":
    main()

