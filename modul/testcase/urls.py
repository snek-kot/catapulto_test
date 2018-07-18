from django.urls import path
from django.urls import path, re_path
from . import views

app_name = 'case'
urlpatterns = [
    path('', views.CaseListView.as_view(), name='list'),
    path('list/', views.CaseListView.as_view(), name='list'),
    path('new/', views.NewView.as_view(), name='new'),
    re_path(r'^view/(?P<pk>\d+)$', views.ViewDetailView.as_view(), name='view'),
    re_path(r'^edit/(?P<pk>\d+)$', views.EditDetailView.as_view(), name='edit'),
]