from django.conf.urls import url
from . import views

app_name = 'notification'

urlpatterns = [
    url(r'^$', views.loginview, name='login'),
]