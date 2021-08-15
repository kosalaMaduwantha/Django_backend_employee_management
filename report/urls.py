from django.urls import path
from . import views

urlpatterns = [
    path('report', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('report/data', views.pivot_data, name='pivot_data'),
]
