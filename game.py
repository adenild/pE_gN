from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

font = ('Arial', '10')


class App:

    def demo(self):

        self.root = tk.Tk()
        self.root.title("ttk.Notebook")


        #Renderizar aqui os menus
        self.nb = ttk.Notebook(self.root)
        self.page1 = ttk.Frame(self.nb)
        self.nb.add(self.page1, text='Dados Gerais')
        self.nb.pack(expand=1, fill="both")

        self.page2 = ttk.Frame(self.nb)
        self.nb.add(self.page2, text='Saldo')




        #Até aqui

        #Dados Gerais
        self.progress = ttk.Progressbar(self.page1, length=500)
        self.progress.pack(padx=15, pady=45)

        self.day_button = ttk.Button(self.page1, text='Clique aqui para mostrar que clicou')
        self.day_button.bind('<Button-1>', self.carregar)
        self.day_button.pack(pady=2)

        #Saldo
        self.valor = 0
        self.saldo = ttk.Label(self.page2, text=f'Saldo: {self.valor}')
        self.saldo.pack(fill='both')

        self.progress.pack()
        self.saldo.pack()

        self.root.mainloop()

    def carregar(self,event):
        update = 2
        self.progress.step(update)
        self.valor += 100
        self.saldo.config(text=f'Saldo: {self.valor}')


if __name__ == "__main__":
    App().demo()
