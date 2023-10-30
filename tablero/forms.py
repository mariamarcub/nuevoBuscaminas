#El formulario tengo que ligarlo al archivo de la vista

from django import forms

#Le indico las características que deben cumplir los recuadros que darán lugar al tablero 
class CreaTableroForm(forms.Form):
    filas = forms.IntegerField(label='Filas',min_value=1, max_value=20, required= True, initial=2)
    columnas = forms.IntegerField(label='Columnas', min_value=1, max_value=15, required=True, initial=2)