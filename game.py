from tkinter import ttk
import tkinter as tk

font = ('Arial', '10')


class App:

    def demo(self):

        self.root = tk.Tk()
        self.root.title("ttk.Notebook")


        #Renderizar aqui os menus
        self.nb = ttk.Notebook(self.root)
        self.nb.pack(expand=1, fill="both")

        self.page1 = ttk.Frame(self.nb)
        self.nb.add(self.page1, text='Dados Gerais')

        self.page2 = ttk.Frame(self.nb)
        self.nb.add(self.page2, text='Saldo')

        self.page3 = ttk.Frame(self.nb)
        self.nb.add(self.page3, text='Trabalho')
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

        #Trabalho
        self.dicionario_pedreiro = {'Ajudante de Pedreiro': 50, 'Pedreiro': 100, 'Mestre de Obras': 500}
        self.dicionario_padeiro = {'Ajudante de Padeiro': 45, 'Padeiro': 95,  'Confeiteiro': 700}
        self.dicionario_programador = {'Aprendiz de Programador': 55, 'Programador Iniciante': 150,
                                       'Programador Experiente': 650}
        self.dicionario_mecanico = {'Aprendiz de Mecânico': 30, 'Gerente de Peças': 150, 'Mecânico Chefe': 1000}
        self.dicionario_corretor = {'Corretor Novato': 40, 'Corretor da Bolsa': 60, 'Chefe Corretor': 900}

        self.trabalhos_disponiveis = ttk.Button(self.page3, text=(
            f"Ajudante de Pedreiro: {self.dicionario_pedreiro['Ajudante de Pedreiro']}"), command=self.definir_status_trabalhando)
        self.trabalhos_disponiveis2 = ttk.Button(self.page3, text=(
            f"Ajudante de Padeiro: {self.dicionario_padeiro['Ajudante de Padeiro']}"))
        self.trabalhos_disponiveis3 = ttk.Button(self.page3, text=(
            f"Aprendiz de Programador: {self.dicionario_programador['Aprendiz de Programador']}"))
        self.trabalhos_disponiveis4 = ttk.Button(self.page3, text=(
            f"Aprendiz de Mecânico: {self.dicionario_mecanico['Aprendiz de Mecânico']}"))
        self.trabalhos_disponiveis5 = ttk.Button(self.page3, text=(
            f"Corretor Novato: {self.dicionario_corretor['Corretor Novato']}"))

        self.trabalhando = False

        '''
        if self.trabalhando == False:

            self.trabalhos_disponiveis.bind('<Button-1>', self.definir_status_trabalhando)
            self.trabalhos_disponiveis2.bind('<Button-1>', self.definir_status_trabalhando)
            self.trabalhos_disponiveis3.bind('<Button-1>', self.definir_status_trabalhando)
            self.trabalhos_disponiveis4.bind('<Button-1>', self.definir_status_trabalhando)
            self.trabalhos_disponiveis5.bind('<Button-1>', self.definir_status_trabalhando)

            self.trabalhos_disponiveis.pack()
            self.trabalhos_disponiveis2.pack()
            self.trabalhos_disponiveis3.pack()
            self.trabalhos_disponiveis4.pack()
            self.trabalhos_disponiveis5.pack()

        else:
            self.erro = ttk.Label(self.page3, text='Erro!')
            self.erro.pack()
        '''
        #testes de funcionalidades
        self.OPTIONS = [
            f"Ajudante de Pedreiro: {self.dicionario_pedreiro['Ajudante de Pedreiro']}",
            f"Ajudante de Padeiro: {self.dicionario_padeiro['Ajudante de Padeiro']}",
            f"Aprendiz de Programador: {self.dicionario_programador['Aprendiz de Programador']}",
            f"Aprendiz de Mecânico: {self.dicionario_mecanico['Aprendiz de Mecânico']}",
            f"Corretor Novato: {self.dicionario_corretor['Corretor Novato']}",
        ]  # etc

        self.variable = tk.StringVar(self.root)
        self.variable.set(self.OPTIONS[0])  # default value

        self.w = ttk.OptionMenu(self.page3, self.variable, *self.OPTIONS)

        self.trabalhos_disponiveis.pack()
        self.w.pack()
        self.progress.pack()
        self.saldo.pack()

        self.root.mainloop()

    def definir_status_trabalhando(self):
        self.trabalhando = True
        print(self.trabalhando)

    def carregar(self,event):
        update = 2
        self.progress.step(update)
        self.valor += 100
        self.saldo.config(text=f'Saldo: {self.valor}')


if __name__ == "__main__":
    App().demo()