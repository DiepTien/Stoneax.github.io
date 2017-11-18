from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$', views.linhvuc.as_view(),name='linhvuc'),
    url(r'^dangki/$',views.dangki,name='dangki'),
    url(r'^dangnhap/$',auth_views.login,{'template_name':'Trangchu/Dangnhap.html'},name='dangnhap'),
    url(r'^dangxuat/$',auth_views.logout,{'next_page':'/'},name='dangxuat'),
    url(r'^(?P<asdddd>\w+)/$',views.cacsanpham.as_view(),name='cacsanpham'),
]
