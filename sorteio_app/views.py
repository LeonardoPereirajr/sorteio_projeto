from django.shortcuts import render, redirect
import csv
import random
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def sorteio(request):
    ganhador = request.session.get('ganhador', None)
    return render(request, 'sorteio_app/sorteio.html', {'ganhador': ganhador})

def login(request):
    return render(request, 'sorteio_app/login.html')

def sorteio_upload(request):
    print("Entrou no sorteio_upload")
    ganhador = None  # Inicialize ganhador como None por padrão
    fs = FileSystemStorage(location='/tmp')

    if request.method == 'POST':
        myfile = request.FILES.get('myfile')  # Obtenha o arquivo do formulário

        if myfile:
            # Salve o arquivo no sistema de arquivos temporário
            filename = fs.save(myfile.name, myfile)

            # Abra o arquivo salvo e leia os nomes
            with open(fs.path(filename), 'r', encoding='utf-8') as csvfile:
                leitor_csv = csv.reader(csvfile)
                nomes = [linha[0] for linha in leitor_csv]

            print("Upload", nomes)

            # Obtenha a lista de nomes já sorteados da sessão ou inicialize uma nova lista vazia
            nomes_sorteados = request.session.get('nomes_sorteados', [])

            if nomes:
                # Remova os nomes já sorteados da lista de nomes
                nomes_disponiveis = [nome for nome in nomes if nome not in nomes_sorteados]

                if nomes_disponiveis:
                    # Faça o sorteio e atualize a sessão com o ganhador
                    ganhador = random.choice(nomes_disponiveis)
                    request.session['ganhador'] = ganhador

                    # Adicione o ganhador à lista de nomes sorteados
                    nomes_sorteados.append(ganhador)
                    request.session['nomes_sorteados'] = nomes_sorteados
                else:
                    ganhador = 'Todos os nomes já foram sorteados.'
            else:
                ganhador = 'Não há nomes para sortear.'
            print("Upload", ganhador)

    return render(request, 'sorteio_app/sorteio.html', {'ganhador': ganhador})
# def sorteio_upload(request):
    # print("Entrou no sorteio_upload")
    # ganhador = None  # Inicialize ganhador como None por padrão
    # fs = FileSystemStorage(location='/tmp')
    
    # # Caminho do arquivo desejado
    # arquivo_caminho = 'C:/Users/leojr/Downloads/sorteio_projeto/resultado.csv'

    # with open(arquivo_caminho, 'r', encoding='utf-8') as csvfile:
    #     leitor_csv = csv.reader(csvfile)
    #     nomes = [linha[0] for linha in leitor_csv]
    # print("Upload", nomes)

    # if nomes:
    #     ganhador = random.choice(nomes)
    #     request.session['ganhador'] = ganhador
    # else:
    #     ganhador = 'Não há nomes para sortear.'
    # print("Upload", ganhador)

    # return render(request, 'sorteio_app/sorteio.html', {'ganhador': ganhador})