from django.urls import path
from . import views

urlpatterns = [
    path( '', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portafolio/', views.portafolio, name='portafolio'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('legal/', views.legal, name='legal'),


]