from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet,index

# Crear un enrutador y registrar el viewset de Car
router = DefaultRouter()
router.register(r'cars', CarViewSet)

# Incluir las URLs del enrutador en las rutas del proyecto
urlpatterns = [
    path('', index, name='index'),
]