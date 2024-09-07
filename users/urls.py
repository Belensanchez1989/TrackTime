from django.urls import include, path
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register("users", views.UserView, "users")

#App ,rutas de la aplicación

urlpatterns = [
    #nombre de la ruta de entrada de la Api
    path('', include(router.urls)),
]
