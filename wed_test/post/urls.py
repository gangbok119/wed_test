from django.conf.urls import url

from .views import post_list, post_detail, post_create, post_delete

urlpatterns = [
    url(r'post/$', post_list, name='post_list'),
    url(r'post/(?P<pk>\d+)/$',post_detail, name='post_detail'),
    url(r'post/create',post_create,name='post_create'),
    url(r'post/delete/(?P<pk>\d+)/$', post_delete, name='post_delete'),

]
