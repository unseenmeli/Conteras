from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.load, name="Conteras-load"),
    path('choose/', views.choose, name="Conteras-choose"),
    path('fhome/', views.fhome, name="Conteras-fhome"),
    path('mhome/', views.mhome, name="Conteras-mhome"),
    path('settings/', views.settings, name="Conteras-settings")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

