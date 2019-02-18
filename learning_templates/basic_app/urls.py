from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
	path(r'^other/$', views.other, name='name'),
	path(r'^relative/$', views.relative, name='relative'),
]