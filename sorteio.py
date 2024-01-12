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

        # Criar uma janela personalizada
        root = tk.Tk()
        root.title('Resultado do Sorteio')

        largura_janela = 400
        altura_janela = 200

        # Obter a resolução da tela
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()

        # Calcular a posição central da janela
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2

        # Definir a geometria da janela
        root.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

        # Exibir mensagem de diálogo
        mensagem = f'O ganhador do sorteio é:\n\n{ganhador}'
        messagebox.showinfo('Ganhador do Sorteio', mensagem)

        # Finalizar o loop principal do tkinter
        root.destroy()

    else:
        print('Não há nomes para sortear.')

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
arquivo_csv = 'C:/Users/leojr/Downloads/Sorteio/resultado.csv'
sortear_ganhador(arquivo_csv)
