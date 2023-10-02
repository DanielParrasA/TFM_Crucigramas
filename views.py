from django.http import HttpResponse, JsonResponse
from .models import Cruc2022
from django.shortcuts import get_object_or_404, render, redirect
import random


# Create your views here.
def index(request):
    title = "aaa"
    return render(request, 'index.html', {
        'title': title
    })

def obtener_pista(request, palabra_obtenida):
    try:
        print(palabra_obtenida)

        pistas = Cruc2022.objects.filter(Palabra=palabra_obtenida)


        if pistas:

            columna_aleatoria = random.choice(['Temperatura_2', 'Temperatura_7'])

            valor_pista = getattr(pistas[0], columna_aleatoria)

            return JsonResponse({'pista': valor_pista})

    except Exception as e:
        return JsonResponse({'error': str(e)})


def obtener_palabra(request, letras):
    primera_letra = request.GET.get('primera_letra', None)
    segunda_letra = request.GET.get('segunda_letra', None)
    tercera_letra = request.GET.get('tercera_letra', None)
    cuarta_letra = request.GET.get('cuarta_letra', None)
    quinta_letra = request.GET.get('quinta_letra', None)
    sexta_letra = request.GET.get('sexta_letra', None)
    septima_letra = request.GET.get('septima_letra', None)
    octava_letra = request.GET.get('octava_letra', None)
    novena_letra = request.GET.get('novena_letra', None)
    decima_letra = request.GET.get('decima_letra', None)
    decimo_primera_letra = request.GET.get('decimo_primera_letra', None)
    decimo_segunda_letra = request.GET.get('decimo_segunda_letra', None)
    decimo_tercera_letra = request.GET.get('decimo_tercera_letra', None)
    decimo_cuarta_letra = request.GET.get('decimo_cuarta_letra', None)
    decimo_quinta_letra = request.GET.get('decimo_quinta_letra', None)


    try:

        # Obtener una palabra aleatoria de la base de datos que coincida con las condiciones
        palabras = Cruc2022.objects.filter(Letras=letras)

        if primera_letra is not None and primera_letra != "null":
            palabras = palabras.filter(_1a_letra=primera_letra)
        if segunda_letra is not None and segunda_letra != "null":
            palabras = palabras.filter(_2a_letra=segunda_letra)
        if tercera_letra is not None and tercera_letra != "null":
            palabras = palabras.filter(_3a_letra=tercera_letra)
        if cuarta_letra is not None and cuarta_letra != "null":
            palabras = palabras.filter(_4a_letra=cuarta_letra)
        if quinta_letra is not None and quinta_letra != "null":
            palabras = palabras.filter(_5a_letra=quinta_letra)
        if sexta_letra is not None and sexta_letra != "null":
            palabras = palabras.filter(_6a_letra=sexta_letra)
        if septima_letra is not None and septima_letra != "null":
            palabras = palabras.filter(_7a_letra=septima_letra)
        if octava_letra is not None and octava_letra != "null":
            palabras = palabras.filter(_8a_letra=octava_letra)
        if novena_letra is not None and novena_letra != "null":
            palabras = palabras.filter(_9a_letra=novena_letra)
        if decima_letra is not None and decima_letra != "null":
            palabras = palabras.filter(_10a_letra=decima_letra)
        if decimo_primera_letra is not None and decimo_primera_letra != "null":
            palabras = palabras.filter(_11a_letra=decimo_primera_letra)
        if decimo_segunda_letra is not None and decimo_segunda_letra != "null":
            palabras = palabras.filter(_12a_letra=decimo_segunda_letra)
        if decimo_tercera_letra is not None and decimo_tercera_letra != "null":
            palabras = palabras.filter(_13a_letra=decimo_tercera_letra)
        if decimo_cuarta_letra is not None and decimo_cuarta_letra != "null":
            palabras = palabras.filter(_14a_letra=decimo_cuarta_letra)
        if decimo_quinta_letra is not None and decimo_quinta_letra != "null":
            palabras = palabras.filter(_15a_letra=decimo_quinta_letra)

        if palabras:
            palabra = random.choice(palabras)
            return JsonResponse({'palabra': palabra.Palabra})
        else:

            return JsonResponse({'error': 'No se encontraron palabras que coincidan con las letras especificadas.'})

    except Exception as e:
        return JsonResponse({'error': str(e)})
