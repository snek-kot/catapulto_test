from django.urls import path
from django.urls import path, re_path
from . import views

app_name = 'plan'
urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('list/', views.PlanListView.as_view(), name='list'),
    path('new/', views.NewCreateView.as_view(), name='new'),
    re_path(r'^view/(?P<pk>\d+)$', views.ViewDetailView.as_view(), name='view'),
    re_path(r'^edit/(?P<pk>\d+)$', views.EditUpdateView.as_view(), name='edit'),
]
