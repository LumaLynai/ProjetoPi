from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clientes.views import ClientesViewSet
from projetoPi.views import fichasViewSet

router = routers.DefaultRouter()
#router.register('clientes', ClientesViewSet)
router.register('projetoPi', fichasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]