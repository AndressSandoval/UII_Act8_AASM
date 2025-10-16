from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.ver_inventario, name='ver_inventario'),
    path('agregar/', views.agregar_inventario, name='agregar_inventario'),
    path('editar/<int:id>/', views.editar_inventario, name='editar_inventario'),
    path('borrar/<int:id>/', views.borrar_inventario, name='borrar_inventario'),
]