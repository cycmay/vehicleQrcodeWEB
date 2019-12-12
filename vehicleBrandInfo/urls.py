from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static 
from vehicleBrandInfo import views

app_name = 'vehicleBrandInfo'
urlpatterns = [
    url(r'^info/(?P<info_pk>[0-9]+)/$', views.info, name='info'),
    url(r'^form2QRcode', views.form2QRcode, name='form2QRcode'),
    url(r'^fillform', views.fillform, name='fillform'),
]