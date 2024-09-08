from django.urls import include, path
from rest_framework import routers
from .views import DayViewSet, MonthViewSet, YearViewSet

router = routers.DefaultRouter()
router.register(r'days', DayViewSet)
router.register(r'months', MonthViewSet)
router.register(r'years', YearViewSet)

#App ,rutas de la aplicación

urlpatterns = [
    #nombre de la ruta de entrada de la Api
    path('', include(router.urls)),
]