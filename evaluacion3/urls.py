"""
URL configuration for evaluacion3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ventas import views
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('ofertas', views.ofertas, name='ofertas'),
    path('carrito', views.carrito, name='carrito'),
    path('producto/<int:id_producto>', views.producto_seleccionado, name="producto_seleccionado"),
    path('delete/<int:id_producto>', views.delete_producto, name="delete_producto"),
    # path('actualizar_carrito', views.actualizar_carrito, name='actualizar_carrito'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)