from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('logout/', views.deconnect, name='deconnect'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('change_password/', views.change_password, name='change_password'),
    path('<str:link_id>/', views.type_new_password, name='type_new_password'),
]
