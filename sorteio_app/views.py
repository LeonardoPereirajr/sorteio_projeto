from django.shortcuts import render
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
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        # Salva o arquivo no sistema temporário
        fs = FileSystemStorage(location='/tmp')
        filename = fs.save(myfile.name, myfile)

        # Caminho do arquivo salvo
        arquivo_csv = fs.url(filename)

        # Realiza o sorteio com o arquivo CSV
        with open(fs.path(filename), 'r', encoding='utf-8') as csvfile:
            leitor_csv = csv.reader(csvfile)
            nomes = [linha[0] for linha in leitor_csv]

        if nomes:
            ganhador = random.choice(nomes)
            request.session['ganhador'] = ganhador
        else:
            ganhador = 'Não há nomes para sortear.'
        
    return sorteio(request)