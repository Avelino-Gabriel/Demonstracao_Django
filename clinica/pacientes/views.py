from django.shortcuts import render

# Create your views here.
from .models import Paciente
from allauth.account.views import SignupView
from .forms import CustomSignupForm
class CustomSignupView(SignupView):
    form_class = CustomSignupForm

def lista_pacientes(request):
    pacientes = [{'nome': 'Gabriel', 'idade': 19}, {'nome': 'Jamily', 'idade': 20}]
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})

def profile(request):
    idade = 19
    user = {'name' : request.user, 'idade': idade}
    
    return render(request, 'profile.html', {'users': user})

