from django.conf.urls import include, url, patterns
from . import views

urlpatterns = patterns('',

    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail ),
    )