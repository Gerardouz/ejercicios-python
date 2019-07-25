from django.urls import path
from .views import CrearUser




urlpatterns = [ 

	path('user/', CrearUser, name = 'user')


]