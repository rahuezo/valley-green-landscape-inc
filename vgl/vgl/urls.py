from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^services/', include('services.urls'), name='services'),
    url(r'^about/', include('about.urls'), name='about'),
    url(r'^contact/', include('contact.urls'), name='contact'),
    url(r'^$', include('home.urls'), name='home'),
]
