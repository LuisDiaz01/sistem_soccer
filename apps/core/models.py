from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.functional import cached_property

# Create your models here.

class Imagen(models.Model):
	"""docstring for imagen"""
	imagen = models.ImageField(
        upload_to='static/images/',
        null=True,
        blank=True,
        verbose_name='Img'
    )
	def __str__(self):
		return f'{self.imagen}'

# para las personas
class Rol(models.Model):
	"""docstring for Rol"""
	rol=models.CharField(max_length=50)
	def __str__(self):
		return self.rol

# para los pos
class Tipo(models.Model):
	"""docstring for Tipo"""
	name=models.CharField(max_length=50)
	def __str__(self):
		return self.nombre

class Estado(models.Model):
	"""docstring for Estado"""
	name=models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Municipio(models.Model):
	"""docstring for Municipio"""
	name=models.CharField(max_length=50)
	estado=models.ForeignKey(Estado,null=True,blank=True,on_delete=models.CASCADE)
	def __str__(self):
		return '{} - {}'.format(self.name, self.estado)

class Estadio(models.Model):
	nombre=models.CharField(max_length=50)
	direccion=models.ForeignKey(Municipio,null=True,blank=True,on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre

class Red(models.Model):
	"""docstring for Redes"""
	facebook=models.CharField(max_length=50)
	twiter=models.CharField(max_length=50)
	instagram=models.CharField(max_length=50)
	def __str__(self):
		return self.facebook

class Persona(models.Model):
	"""docstring for Persona"""
	imagen = models.OneToOneField(Imagen,blank=True,on_delete=models.CASCADE)
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	cedula=models.IntegerField(unique=True)
	email=models.EmailField()
	edad=models.IntegerField()
	peso=models.IntegerField()
	red=models.ForeignKey(Red,null=True,blank=True,on_delete=models.CASCADE)
	rol=models.ForeignKey(Rol,null=True,blank=True,on_delete=models.CASCADE)
	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)

class Club(models.Model):
	"""docstring for Club"""
	# imagen=models.ForeignKey(Imagen,null=True,blank=True,on_delete=models.CASCADE)
	nombre=models.CharField(max_length=50)
	# datos random
	mision=models.TextField(default='')
	historia=models.TextField(default='')
	directivo=models.ManyToManyField(Persona,blank=True)
	estadio=models.ForeignKey(Estadio,null=True,blank=True,on_delete=models.CASCADE)
	email=models.EmailField(default='xxxxx@xxx.com')
	red=models.ForeignKey(Red,null=True,blank=True,on_delete=models.CASCADE)
	numero_telefono=models.CharField(max_length=50,default='')
	direccion=models.ForeignKey(Municipio,null=True,blank=True,on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre

class Divicion(models.Model):
	"""docstring for Divicion"""
	name=models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Equipo(models.Model):
	"""docstring for Equipo"""
	persona=models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
	club=models.ForeignKey(Club,null=True,blank=True,on_delete=models.CASCADE)
	divicion=models.ForeignKey(
		Divicion,
		null=True,
		blank=True,
		on_delete=models.CASCADE,
	) 
	def __str__(self):
		return self.persona

class Post(models.Model):
	"""docstring for Post"""
	title=models.CharField(max_length=50)
	content=models.TextField()
	date_create=models.DateField()
	tipo=models.ForeignKey(Tipo,null=True,blank=True,on_delete=models.CASCADE)
	imagen=models.ManyToManyField(Imagen,blank=True)
	def __str__(self):
		return self.title

