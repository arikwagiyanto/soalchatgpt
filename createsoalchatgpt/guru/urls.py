from django.urls import path # type: ignore
from .import views
urlpatterns = [
    path('', views.beranda_guru, name='beranda_guru'),
    path('lihatjadwal/', views.lihatjadwal, name='lihatjadwal'),
    path('buatsoal/', views.buatsoal, name='buatsoal'),
]