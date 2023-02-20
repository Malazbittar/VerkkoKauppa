import tkinter as tk

class ShoppingList:
    def __init__(self, master):
        self.master = master
        master.title("Ostoslista")

        self.item_list = []

        self.item_label = tk.Label(master, text="Ostoslista:")
        self.item_label.pack()

        self.item_text = tk.Text(master, height=10, width=50)
        self.item_text.pack()

        self.add_button = tk.Button(master, text="Lisää tuote", command=self.add_item)
        self.add_button.pack()

        self.remove_button = tk.Button(master, text="Poista tuote", command=self.remove_item)
        self.remove_button.pack()

        self.quit_button = tk.Button(master, text="Lopeta", command=master.quit)
        self.quit_button.pack()

    def add_item(self):
        item = input("Lisää tuote: ")
        self.item_list.append(item)
        self.item_text.insert(tk.END, item + "\n")

    def remove_item(self):
        item = input("Poista tuote: ")
        if item in self.item_list:
            self.item_list.remove(item)
            self.item_text.delete(1.0, tk.END)
            for item in self.item_list:
                self.item_text.insert(tk.END, item + "\n")

root = tk.Tk()
my_shopping_list = ShoppingList(root)
root.mainloop()
