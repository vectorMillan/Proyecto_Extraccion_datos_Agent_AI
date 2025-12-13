from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# El decorador @login_required asegura que nadie entre aquí sin iniciar sesión
@login_required
def dashboard_view(request):
    return render(request, 'tesis/dashboard.html')