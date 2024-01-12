from django.shortcuts import render
import csv
import random

def sorteio(request):
    arquivo_csv = 'C:/Users/leojr/Downloads/sorteio_projeto/resultado.csv'  # Substitua pelo caminho correto
    with open(arquivo_csv, 'r', encoding='utf-8') as csvfile:
        leitor_csv = csv.reader(csvfile)
        nomes = [linha[0] for linha in leitor_csv]

    if nomes:
        ganhador = random.choice(nomes)
    else:
        ganhador = 'Não há nomes para sortear.'

    return render(request, 'sorteio_app/sorteio.html', {'ganhador': ganhador})

def login(request):
    return render(request, 'sorteio_app/login.html')