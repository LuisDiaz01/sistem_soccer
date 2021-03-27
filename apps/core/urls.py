from django.urls import path, include
from apps.core.views import List, Create, Update, Delete, Show
app_name='core'
urlpatterns=[
	path('index/',List.as_view(),name='index'),
	path('create/',Create.as_view(),name='create'),
	# path('edit/<int:pk>/',Edit.as_view(),name='edit'),
	path('update/<int:pk>/',Update.as_view(),name='update'),
	path('delete/<int:pk>/',Delete.as_view(),name='delete'),
	path('show/<int:id_mascota>/', Show, name='show'),
]