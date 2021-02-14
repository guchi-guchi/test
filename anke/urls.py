from django.urls import path
from anke import views

app_name='anke'
urlpatterns = [
    path('', views.index, name='index'),
    path('anke/', views.ankeView, name='anke'),
    path('list/', views.ankeList, name='list'),
    path('export/', views.ankeExport, name='export'),
    path('table/', views.tableView, name='table'),
    path('success/', views.successView, name='success'),
]