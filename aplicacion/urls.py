from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),

    path('cortes/', cortes, name="cortes"),
    path('peinados/', peindados, name="peinados"),
    path('estilistas/', estilistas, name="estilistas"),
    
    path('corteForm/', corteForm, name="corteForm"),
    path('peinadoForm/', peinadoForm, name="peinadoForm"),
    path('estilistaForm/', estilistaForm, name="peinadoForm"),

    path('buscarCorte/', buscarCorte, name="buscarCorte"),
    path('buscar_corte/', buscar_corte, name="buscar_corte"),

    path('buscarPeinado/', buscarPeinado, name="buscarPeinado"),
    path('buscar_peinado/', buscar_peinado, name="buscar_peinado"),

    path('buscarEstilista/', buscarEstilista, name="buscarEstilista"),
    path('buscar_estilista', buscar_estilista, name="buscar_estilista"),
    
]
 

