#from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('servicios', views.servicios, name='servicios'),
    path('logoutt', views.logoutt, name='logoutt'),
    path('menu', views.menu, name='menu'),
    path('crear/', views.crear_casa, name='crear_casa'),
    path('editar/<int:id>/', views.editar_casa, name='editar_casa'),
    path('eliminar/<int:id>/', views.eliminar_casa, name='eliminar_casa'),

    path('', views.index, name='index'),
    path('servicios/', views.servicios, name='servicios'),
    path('detalle_casa/<int:casa_id>/', views.detalle_casa, name='detalle_casa'),
    path('casa_delete/<int:id_casa>/', views.casa_delete, name='casa_delete'),
    path('casa_add/', views.casa_add, name='casa_add'),
    path('casa_edit/<int:casa_id>/', views.casa_edit, name='casa_edit'),
    # Otras URLs de tu aplicación inmoss
    path('register/', views.register, name='register'),
    path('pago/<int:id_casa>/', views.pago, name='pago'),
    path('inmoss/proceso_pago/<int:id_casa>/', views.proceso_pago, name='proceso_pago'),
]

