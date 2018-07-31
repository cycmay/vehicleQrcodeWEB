from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static 
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^login', views.login, name='login'),
]