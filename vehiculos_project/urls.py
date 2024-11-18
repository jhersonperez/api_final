from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehiculos/', include('vehiculos.urls')),  # Incluye las rutas de la app 'vehiculos'
    path('', lambda request: HttpResponse("Bienvenido a la API de Vehículos"), name='home'),
]
