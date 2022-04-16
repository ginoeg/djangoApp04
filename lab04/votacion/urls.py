from django.urls import path

from . import views

app_name = 'candidatos'

urlpatterns = [
    #ex: /votacion/
    path('', views.index, name='index'),
    #ex: /votacion/2/
    path('<int:region_id>/', views.listar, name="listar"),
    #ex: /votacion/1/2/detalles
    path('<int:region_id>/<int:candidato_id>/detalles/', views.detalles, name="detalles"),
]