from django.urls import path
from . import views

urlpatterns = [
    path('marcas/', views.listar_marcas, name='listar_marcas'),
    path('marcas/crear/', views.crear_marca, name='crear_marca'),
    path('marcas/<int:id>/editar/', views.actualizar_marca, name='actualizar_marca'),
    path('marcas/<int:id>/eliminar/', views.eliminar_marca, name='eliminar_marca'),
    # Repite para los demás modelos
]
