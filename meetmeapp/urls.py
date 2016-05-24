from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.meeting_list, name='meeting_list'),
]