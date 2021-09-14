from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   url(r'home',views.home,name='home'),
   url(r'entry',views.saveEntry,name='Save Entry'),
   url(r'^request_enter/$',views.carEntered,name='Car Entery'),
   url(r'^request_exit/$',views.carExit,name='Car Exit'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
