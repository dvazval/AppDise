#from django.shortcuts import render
# Create your views here.
# auth/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_user(request):
    state = "Por favor ingrese su nombre de usuario y contrase&ntilde;a para iniciar sessión."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Bienvenido " + username 
            else:
                state = "Su cuenta no esta activada, por favor contacte con el administrador del sitio."
        else:
            state = "Su nombre de usuario y/o contrase&ntilde; a son incorrectos."

    return render(request,'home.html',{'state':state, 'username': username})
