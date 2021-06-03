from django import forms
from apps.core.models import Post, Persona, Equipo


class PostForm(forms.ModelForm):
	"""docstring for MascotaForm"""
	class Meta:
		model=Post
		fields=[
			'title',
			'content',
			'date_create',
			'imagen',
		]
		lebels={
			'title':'Titulo',
			'content':'Contenido',
			'date_create':'Fecha de publicación',
			'imagen':'Imagen',
		}
		widgets={
			'title':forms.TextInput(),
			'content':forms.TextInput(),
			'date_create':forms.NumberInput(),
			'imagen':forms.FileInput(),
		}

# class PersonaForm(forms.ModelForm):
# 	"""docstring for PersonaForm"""
# 	class Meta:
# 		model=Persona
# 		fields=[
# 			'imagen',
# 			'nombre',
# 			'apellido',
# 			'cedula',
# 			'email',
# 			'edad',
# 			'peso',
# 			'red',
			
# 		]
# 		lebels={
# 			'imagen':'Foto',
# 			'nombre':'Nombre',
# 			'apellido':'Apellido',
# 			'cedula':'Cedula de Identidad',
# 			'email':'E-mail',
# 			'edad':'Edad',
# 			'peso':'Peso',
			
# 		}
# 		widgets={
# 			'imagen':forms.FileInput(),
# 			'nombre':forms.TextInput(),
# 			'apellido':forms.TextInput(),
# 			'cedula':forms.NumberInput(),
# 			'email':forms.EmailInput(),
# 			'edad':forms.NumberInput(),
# 			'peso':forms.NumberInput(),
			
# 		}

# class SteamForm(forms.ModelForm):
# 	"""docstring for SteamForm"""
# 	class Meta:
# 		model=Steam
# 		fields=[
# 			'persona',
# 			'club',
# 			'divicion',	
# 		]
# 		lebels={
# 			'persona':'Atleta',
# 			'club':'Club',
# 			'divicion':'Divición',
# 		}