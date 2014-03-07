from django.conf.urls import patterns, include, url
from yellowpenguin import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yellowpenguin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^transactions/', include('transactions.urls', namespace='transactions')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^morrisChartData/transStats', views.morrisChartData, name='morrisChartData')
)
