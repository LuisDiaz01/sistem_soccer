from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.functional import cached_property
from apps.core.models import *
# Create your models here.



class Encuentro(models.Model):
	"""docstring for Encuentro"""
	nombre=models.CharField(max_length=50)
	tipo=models.CharField(max_length=50)
	equivo_casa=models.CharField(max_length=50)
	equipo_invitado=models.CharField(max_length=50)
	goles_invitado=models.IntegerField()
	goles_casa=models.IntegerField()
	def __str__(self):
		return f'Encuentro:{self.nombre}'
