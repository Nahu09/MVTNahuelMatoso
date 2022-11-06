from django.shortcuts import render

from app1.models import Familia
# Create your views here.

def mostrar_familiares(request):
    f1 = Familia(nombre = 'Agustin', edad = 23, cumpleanios = '1999-10-27')

    f2 = Familia(nombre = 'Carlos', edad = 25, cumpleanios = '1997-09-03')

    f3  = Familia(nombre = 'Bautista', edad = 17, cumpleanios = '2005-07-02' )

    return render(request, 'app1/familia.html', {'familia': [f1, f2, f3]})