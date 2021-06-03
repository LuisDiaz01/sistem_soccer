from django.urls import path, include
from apps.landing.views import index, club_info
app_name='landing'
urlpatterns=[
	path('', index, name='index'),
	path('club', club_info, name='club_info'),
]