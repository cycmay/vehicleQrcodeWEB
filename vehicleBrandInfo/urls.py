from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static 
from . import views

app_name = 'vehicleBrandInfo'
urlpatterns = [
    url(r'^info/(?P<info_pk>[0-9]+)/$', views.info, name='info'),
    url(r'^form2QRcode', views.form2QRcode, name='form2QRcode'),
    url(r'^form_to_fill', views.form_to_fill, name='form_to_fill'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)