from django.conf.urls import url
from . import views
from  django.views.generic import ListView,DetailView


urlpatterns=[
    url(r'^$',views.chungloai.as_view(),name='chungloai'),
    url(r'^(?P<Linhkien_id>\w+)$',views.linhkien.as_view(),name='linhkien'),

]
