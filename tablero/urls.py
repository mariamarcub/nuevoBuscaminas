from django.urls import path
from tablero import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('crea_tablero/', views.crea_tablero, name='crea_tablero'), 
]

#Asociamos a una vista llamada views.index a la url raíz
#el name='index' es para darle nombre a esa url que está ligada a la vista

#Asociamos otra vista pero para la página crea_tablero