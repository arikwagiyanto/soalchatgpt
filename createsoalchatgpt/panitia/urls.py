from django.urls import path # type: ignore
from .import views
urlpatterns = [
    path('', views.beranda_panitia, name='beranda_panitia'),
    path('kelolajadwal/', views.kelolajadwal, name='kelolajadwal'),
    path('lihatsoal/', views.lihatsoal, name='lihatsoal'),
    path('cetaksoal/', views.cetaksoal, name='cetaksoal'),
]