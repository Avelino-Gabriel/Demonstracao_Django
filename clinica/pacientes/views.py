from django.shortcuts import render

# Create your views here.
from .models import Paciente

def lista_pacientes(request):
    pacientes = [{'nome': 'Gabriel', 'idade': 19}, {'nome': 'Jamily', 'idade': 20}]
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})

def profile(request):
    user = [{'name' : request.user}]
    return render(request, 'profile.html', {'users': user})

