from django.urls import path

from django.urls import path, re_path
from . import views

app_name = 'account'
urlpatterns = [
    path('signin/', views.NewAccountView.as_view(), name='new_account'),
    path('login/', views.LoginAccountView.as_view(), name='login'),
]