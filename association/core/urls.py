from django.urls import path
from core.views import UserView
from core.views import DashboardView

urlpatterns = [
    path('index/', DashboardView.as_view(),  name='dashboard_index'),
    path('users/', UserView.as_view(),  name='index_users'),
]