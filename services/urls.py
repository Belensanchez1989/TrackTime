from django.urls import include, path
from rest_framework import routers
from services import views

router = routers.DefaultRouter()
router.register("services", views.ServiceView, "services")

#App ,rutas de la aplicación

urlpatterns = [
    #nombre de la ruta de entrada de la Api
    path('', include(router.urls)),
]