from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('thrissur/', views.thrissur_page, name='thrissur'),
    path('kochi/', views.kochi_page, name='kochi'),
    path('kannur/', views.kannur_page, name='kannur'),
    path('palakkad/', views.palakkad_page, name='palakkad'),
    path('malappuram/', views.malappuram_page, name='malappuram'),
    path('form/', views.form_page, name='form'),
]