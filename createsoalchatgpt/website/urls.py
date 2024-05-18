from django.urls import path # type: ignore
from .import views

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('logout/', views.logoutPage, name='logoutPage'),
]