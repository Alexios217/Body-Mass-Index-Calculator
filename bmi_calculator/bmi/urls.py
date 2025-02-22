from django.urls import path
from .views import calculate_bmi

urlpatterns = [
    path('calculate/',calculate_bmi, name='bmi_calculate'),
]
