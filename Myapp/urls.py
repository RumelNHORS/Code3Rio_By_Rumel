from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]