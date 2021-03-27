from django.db import models
# Create your models here.

class Imagen(models.Model):
	"""docstring for imagen"""
	imagen = models.ImageField(
        upload_to='static/img_post/',
        null=True,
        blank=True,
        verbose_name='Post'
    )
	def __str__(self):
		return '{}'.format(self.imagen)
class Tipo(models.Model):
	"""docstring for Tipo"""
	nombre=models.CharField(max_length=50)
	def __str__(self):
		return '{}'.format(self.nombre)

class Post(models.Model):
	"""docstring for Mascota"""
	title=models.CharField(max_length=50)
	content=models.TextField()
	date_create=models.DateField()
	tipo=models.ForeignKey(Tipo,null=True,blank=True,on_delete=models.CASCADE)
	imagen=models.ManyToManyField(Imagen,blank=True)
	def __str__(self):
		return '{}'.format(self.title)

class Rol(models.Model):
	"""docstring for Rol"""
	rol=models.CharField(max_length=50)
	def __str__(self):
		return '{}'.format(self.rol)

class Persona(models.Model):
	"""docstring for Persona"""
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	cedula=models.IntegerField()
	telefono=models.CharField(max_length=12)
	email=models.EmailField()
	domicilio=models.TextField()
	edad=models.IntegerField()
	rol=models.ForeignKey(Rol,null=True,blank=True,on_delete=models.CASCADE)
	def __str__(self):
		return '{} {}'.format(self.nombre,self.apellido)

class Perfil(models.Model):
	"""docstring for Profile Ministerio"""
	nombre=models.CharField(max_length=50)
	mision=models.TextField()
	fecha_creado=models.DateField()
	direccion=models.CharField(max_length=50)
	integrante=models.ManyToManyField(Persona,blank=True)
	def __str__(self):
		return '{}'.format(self.nombre)
		