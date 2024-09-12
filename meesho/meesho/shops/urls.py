from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # root URL points to home
    # path('home/', views.index, name='index'),  # home/ URL points to index
]
