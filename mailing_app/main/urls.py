from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('account/<int:pk>/profile/', views.ProfileUpdate.as_view(), name="profile"),
]