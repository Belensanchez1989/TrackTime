from django.urls import include, path
from rest_framework import routers
from hours import views

router = routers.DefaultRouter()
router.register("hours", views.HourView, "hours")

#App ,rutas de la aplicación

urlpatterns = [
    #nombre de la ruta de entrada de la Api
    path('', include(router.urls)),
]