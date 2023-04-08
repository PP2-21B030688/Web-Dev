from django.urls import path
from . import views

urlpatterns = [
    path('companies/create/', views.createCompany),
    path('companies/delete/', views.deleteCompanies),
    path('companies/', views.getCompanies),
    path('companies/<int:pk>/', views.getCompany),
    path('companies/<int:pk>/vacancies/', views.getVacanciesByCompany),
    path('vacancies/create/', views.createVacancy),
    path('vacancies/delete/', views.deleteVacancies),
    path('vacancies/', views.getVacancies),
    path('vacancies/<int:pk>/', views.getVacancy),
    path('vacancies/top/', views.getTopVacancies),
]