from django.urls import path
from anke import views

app_name='anke'
urlpatterns = [
    path('', views.index, name='index'),
    path('anke/', views.ankeView, name='anke'),
    path('list/', views.ankeList, name='list'),
    path('export/', views.ankeExport, name='export'),
    path('gift/', views.giftView, name='gift'),
    path('table/', views.tableView, name='table'),
    path('ka_list/', views.ankeList_ka, name='ka_list'),
    path('ka_export/', views.ankeKapaExport, name='ka_export'),
]