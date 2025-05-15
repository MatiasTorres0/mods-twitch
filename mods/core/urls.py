from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('inicio', views.inicio, name='inicio'),
    path('comandos', views.comandos, name='comandos'),
    path('protocolos', views.protocolos, name='protocolos'),
    path('anuncios', views.anuncios, name='anuncios'),
    path('logout/', views.logout_view, name='logout'),
    path('agregar_comando/', views.agregar_comando, name='agregar_comando'),
]

