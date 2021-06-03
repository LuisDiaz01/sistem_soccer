from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.core.form import PostForm
from apps.core.models import Post


# Create your views here.

def Show(request,id_post):
	post=Post.objects.get(id=id_post)
	context={'post':post}
	return render(request,'post/show.html',context)

class List(ListView):
	"""docstring for MascotaList"""
	model=Post
	template_name='post/list.html'

class Create(CreateView):
	"""docstring for MascotaCreate"""
	model=Post
	form_class=PostForm
	template_name='post/view.html'
	success_url=reverse_lazy('post:show')

class Update(UpdateView):
	"""docstring for MascotaCreate"""
	model=Post
	form_class=PostForm
	template_name='post/view.html'
	success_url=reverse_lazy('post:show')

class Delete(DeleteView):
	"""docstring for MascotaDelete"""
	model=Post
	template_name='post/delete.html'
	success_url=reverse_lazy('post:show')
	
	