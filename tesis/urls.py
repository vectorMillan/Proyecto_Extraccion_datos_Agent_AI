from django.urls import path
from . import views

urlpatterns = [
    # Cuando entran a la raíz o a /dashboard, ven el panel
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Redirigimos la raíz ('') al dashboard también
    path('', views.dashboard_view, name='home'),
]