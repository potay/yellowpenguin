from django.conf.urls import patterns, url

from transactions import views

urlpatterns = patterns('',
	# ex: /transactions/
    url(r'^$', views.index, name='index'),
    # ex: /transactions/5/
    url(r'^(?P<trans_id>\d+)/$', views.detail, name='detail'),
    # ex: /transactions/5/edit/
    url(r'^(?P<trans_id>\d+)/edit/$', views.edit, name='edit'),
    # ex: /transactions/add/
    url(r'add/$', views.add, name='add'),
)