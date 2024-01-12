import re
import csv

def extrair_nomes_perfil(arquivo_csv_entrada, arquivo_csv_saida):
    with open(arquivo_csv_entrada, 'r', encoding='utf-8') as file:
        linhas_originais = file.readlines()

    nomes_perfil = []

    for linha_perfil in linhas_originais:
        match = re.search(r'Foto do perfil de (.+)', linha_perfil)
        
        if match:
            nome_perfil = match.group(1).split('@')[0].strip()
            nomes_perfil.append(nome_perfil)

    with open(arquivo_csv_saida, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for nome in nomes_perfil:
            csvwriter.writerow([nome])

    print(f'Foram extraidos {len(nomes_perfil)} nomes de perfil.')

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
arquivo_csv_entrada = 'C:/Users/leojr/Downloads/Sorteio/comentarios.csv'
arquivo_csv_saida = 'C:/Users/leojr/Downloads/Sorteio/resultado.csv'
extrair_nomes_perfil(arquivo_csv_entrada, arquivo_csv_saida)
