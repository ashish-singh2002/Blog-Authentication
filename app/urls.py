from django.urls import path,include
from .import views

urlpatterns = [  
    path('',views.register,name="register"),       
    path('login/',views.login,name="login"),
    path('home/',views.home,name="home"),
    path('read/',views.read,name="read"),
    path('<int:id>/edit/',views.edit,name="edit"),
    path('<int:id>/delete/',views.delete,name="delete"),


]
