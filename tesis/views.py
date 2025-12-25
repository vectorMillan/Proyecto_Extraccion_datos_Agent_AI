from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tesis
from .forms import TesisForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# El decorador @login_required asegura que nadie entre aquí sin iniciar sesión
@login_required
def dashboard_view(request):
    return render(request, 'tesis/dashboard.html')

# 1. LISTAR TESIS (Read)
class TesisListView(LoginRequiredMixin, ListView):
    model = Tesis
    template_name = 'tesis/tesis_list.html'
    context_object_name = 'tesis'
    ordering = ['-created_at'] # Las más nuevas primero

# 2. CREAR TESIS MANUALMENTE (Create)
class TesisCreateView(LoginRequiredMixin, CreateView):
    model = Tesis
    form_class = TesisForm
    template_name = 'tesis/tesis_form.html'
    success_url = reverse_lazy('tesis_list') # Al terminar, nos manda a la lista

    # Este método es vital: Asigna automáticamente el usuario que está logueado
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

# 3. EDITAR TESIS (Update)
class TesisUpdateView(LoginRequiredMixin, UpdateView):
    model = Tesis
    form_class = TesisForm
    template_name = 'tesis/tesis_form.html' # Reutilizamos el mismo template de crear
    success_url = reverse_lazy('tesis_list')

# 4. ELIMINAR TESIS (Delete)
class TesisDeleteView(LoginRequiredMixin, DeleteView):
    model = Tesis
    template_name = 'tesis/tesis_confirm_delete.html'
    success_url = reverse_lazy('tesis_list')

