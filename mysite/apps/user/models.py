from django.db import models

# Create your models here.


class User(models.Model):

	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 100, blank = False, null = False)
	apellido = models.CharField(max_length = 100, blank = False, null = False)

	cedula = models.IntegerField(blank = False, null = False)

	class Meta():
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'
		ordering = ['nombre']

	def __str__(self):

		return self.nombre



class Auto(models.Model):

	id = models.AutoField(primary_key = True)

	modelo = models.CharField(max_length = 100, blank = False, null = False)

	placa = models.IntegerField(blank = False, null = False)


	dueño = models.OneToOneField(User, on_delete = models.CASCADE)

	class Meta():

		verbose_name = 'Auto'
		verbose_name_plural = 'Autos'

		ordering = ['modelo']

	def __str__(self):

		return self.modelo

