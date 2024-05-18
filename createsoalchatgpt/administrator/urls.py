from django.urls import path # type: ignore
from .import views
urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('pengguna/', views.pengguna, name='pengguna'),
    path('cekjadwal/', views.cekjadwal, name='cekjadwal'),
    path('ceksoal/', views.ceksoal, name='ceksoal'),
]