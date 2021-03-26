from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('account/<int:pk>/profile/', views.ProfileDetailView.as_view(), name="profile"),
    path('account/<int:pk>/edit/', views.ProfileUpdate.as_view(), name="profile_edit"),
]