from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/', views.CompanyList.as_view(), name='company'),
    path('employeer/', views.EmployeerList.as_view(), name='employeer'),
    path('company/<str:cnpj>', views.Filtercompany.as_view(), name='company'),
    path('employeer/<str:username>/', views.Filteremployeer.as_view(), name='employeer'),
]
