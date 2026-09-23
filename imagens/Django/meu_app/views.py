from django.shortcuts import render

def home(request):
    # Lógica em Python: renderiza o arquivo template .html
    return render(request, 'home.html')
