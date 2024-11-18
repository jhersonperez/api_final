from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Marca
from .forms import MarcaForm
from django.http import HttpResponse
from django.http import JsonResponse
import json

def home(request):
    return HttpResponse("<h1>Bienvenido a la aplicación Vehículos</h1>")

def listar_marcas(request):
    if request.method == 'GET':
        marcas = Marca.objects.all().values('id', 'nombre')  # Asegúrate de que tu modelo se llame 'Marca'
        return JsonResponse(list(marcas), safe=False)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def crear_marca(request):
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)  # Cargar datos enviados en formato JSON
            nueva_marca = Marca.objects.create(nombre=datos['nombre'])
            return JsonResponse({'id': nueva_marca.id, 'nombre': nueva_marca.nombre}, status=201)
        except KeyError:
            return JsonResponse({'error': 'El campo "nombre" es obligatorio'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'El cuerpo de la solicitud debe ser JSON válido'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def actualizar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'vehiculos/actualizar_marca.html', {'form': form})

def eliminar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    if request.method == 'POST':
        marca.delete()
        return redirect('listar_marcas')
    return render(request, 'vehiculos/eliminar_marca.html', {'marca': marca})
