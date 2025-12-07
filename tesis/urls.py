from django.urls import path
from . import views

urlpatterns = [
    # Cuando entran a la raíz o a /dashboard, ven el panel
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Redirigimos la raíz ('') al dashboard también
    path('', views.dashboard_view, name='home'),
    # CRUD Tesis
    path('tesis/', views.TesisListView.as_view(), name='tesis_list'), # Lista
    path('tesis/create/', views.TesisCreateView.as_view(), name='tesis_create'), # Crear
    path('tesis/edit/<int:pk>/', views.TesisUpdateView.as_view(), name='tesis_edit'), # Editar
    path('tesis/delete/<int:pk>/', views.TesisDeleteView.as_view(), name='tesis_delete'), # Eliminar
]