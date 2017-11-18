from django.conf.urls import url

from . import views

app_name = 'services'

urlpatterns = [
    url(r'^$', views.services_view, name='services'),
]
