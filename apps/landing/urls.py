from django.urls import path, include
from apps.landing.views import index, index2, club_info
app_name='landing'
urlpatterns=[
	path('', index, name='index'),
	path('index2', index2, name='index2'),
	path('club', club_info, name='club_info'),
]