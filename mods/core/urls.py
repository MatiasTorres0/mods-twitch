from django.db import router
from django.urls import path
from django.contrib.auth import views as auth_views
from django.utils.translation import round_away_from_one
from . import views
from .views import upload_excel_comandos
from rest_framework import routers
from django.urls.conf import include


router = routers.DefaultRouter()
router.register('comandos', views.ComandoViewSet)
router.register('moderadores', views.ModeradorViewSet)
router.register('notas', views.NotasViewSet)
router.register('combates', views.CombateViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('inicio/', views.inicio, name='inicio'),  # Added trailing slash
    path('comandos/', views.comandos, name='comandos'),  # Added trailing slash
    path('protocolos/', views.protocolos, name='protocolos'),  # Added trailing slash
    path('anuncios/', views.anuncios, name='anuncios'),  # Added trailing slash
    path('logout/', views.logout_view, name='logout'),
    path('agregar_comando/', views.agregar_comando, name='agregar_comando'),
    path('editar_comando/<int:comando_id>/', views.editar_comando, name='editar_comando'),
    path('eliminar_comando/<int:comando_id>/', views.eliminar_comando, name='eliminar_comando'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('comandos/upload-excel/', upload_excel_comandos, name='upload_excel_comandos'),
    path('api/', include(router.urls)),
    path('politicas_uso_app/', views.politicas_uso_app, name='politicas_uso_app'),
    path('notas_mods/', views.notas_mods, name='notas_mods'),
    path('agregar_combate/', views.agregar_combate, name='agregar_combate'),
    path('seccion_agregar/', views.seccion_agregar, name='seccion_agregar'),
    path('ver_notas/', views.ver_notas, name='ver_notas'),
    path('subir_excel_combate/', views.subir_excel_combate, name='subir_excel_combate'),
    path('ver_combates/', views.ver_combates, name='ver_combates'),
    path('editar_nota/<int:nota_id>/', views.editar_nota, name='editar_nota'),
    path('eliminar_nota/<int:nota_id>/', views.eliminar_nota, name='eliminar_nota'),
]

