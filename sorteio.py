import csv
import random
import tkinter as tk
from tkinter import messagebox

def sortear_ganhador(arquivo_csv):
    with open(arquivo_csv, 'r', encoding='utf-8') as csvfile:
        leitor_csv = csv.reader(csvfile)
        nomes = [linha[0] for linha in leitor_csv]

    if nomes:
        ganhador = random.choice(nomes)

        root = tk.Tk()
        root.title('Resultado do Sorteio')

        largura_janela = 400
        altura_janela = 200

        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()

        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2

        root.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

        mensagem = f'O ganhador do sorteio é:\n\n{ganhador}'
        messagebox.showinfo('Ganhador do Sorteio', mensagem)

        root.destroy()

    else:
        print('Não há nomes para sortear.')

arquivo_csv = 'C:/Users/leojr/Downloads/Sorteio/resultado.csv'
sortear_ganhador(arquivo_csv)
