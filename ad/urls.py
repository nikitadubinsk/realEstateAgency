from django.urls import path
from . import views

urlpatterns = [
  path('ads/', views.AdListView.as_view()),
  path('ad/<int:pk>/', views.AdDetailView.as_view()),
  path('convenience/', views.СonvenienceCreateView.as_view())
]