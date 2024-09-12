from django.urls import include, path
from rest_framework import routers
from reservations import views

router = routers.DefaultRouter()
router.register("reservations", views.ReservationView, "reservations")

#App ,rutas de la aplicación

urlpatterns = [
    #nombre de la ruta de entrada de la Api
    path('', include(router.urls)),
]