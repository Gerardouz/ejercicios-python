from django.urls import path,re_path
from .views import CrearUser,ConsultaUser,EditUser,ElimUser




urlpatterns = [ 

	path('user/', CrearUser, name = 'user'),
	path('consult_user/', ConsultaUser , name = 'consult_user'),
	path('edit_user/<int:id>', EditUser, name = 'edit_user'),
	path('elim_user/<int:id>', ElimUser, name = 'elim_user'),

]