from django.conf.urls import url
from .views import *

urlpatterns = {
    url(r'^$', home, name = 'index'),
    url(r'^crear_usuario/',crearUser, name = 'crear_user'),
}