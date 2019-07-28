from django.conf.urls import url
from blog import views

# app_name = 'blog'
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^edit/(?P<pk>\d+)/$', views.post_edit, name='post_edit'),
	url(r'^about/$', views.about, name='about')
]