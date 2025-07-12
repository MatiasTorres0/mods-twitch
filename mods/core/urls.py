from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import upload_excel_comandos

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
]

