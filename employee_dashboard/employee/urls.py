from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeesView.as_view()),
]
