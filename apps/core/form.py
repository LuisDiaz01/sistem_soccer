from django import forms
from apps.core.models import Post


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

	# def __init__(self, arg):
	# 	super(MascotaForm, self).__init__()
	# 	self.arg = arg

