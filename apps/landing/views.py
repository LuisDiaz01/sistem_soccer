from django.shortcuts import render
from apps.core.models import Post, Club
from pdb import set_trace
# Create your views here.

def index(request):
	post=Post.objects.all().order_by('id')
	club=Club.objects.all().order_by('id')
	context={
		'post':post,
		'club':club
		}
	return render(request, 'landing/index.html', context)

def index2(request):
	post=Post.objects.all().order_by('id')
	club=Club.objects.all().order_by('id')
	context={
		'post':post,
		'club':club
		}
	return render(request, 'landing/index2.html', context)

def club_info(request):
	club=Club.objects.all().order_by('id')
	context={'club':club}
	return render(request, 'landing/club_info.html', context)
