from django.urls import path, include
from apps.core.views import List, Create, Update, Delete, Show
app_name='core'
urlpatterns=[
	path('indexPost/',List.as_view(),name='index'),
	path('createPost/',Create.as_view(),name='create'),
	# path('edit/<int:pk>/',Edit.as_view(),name='edit'),
	path('updatePost/<int:pk>/',Update.as_view(),name='update'),
	path('deletePost/<int:pk>/',Delete.as_view(),name='delete'),
	path('showPost/<int:id_mascota>/', Show, name='show'),
]