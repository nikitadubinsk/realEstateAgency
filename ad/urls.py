from django.urls import path
from . import views
from workers.models import Realtor, Position

urlpatterns = [
  path('ads/', views.AdListView.as_view()),
  path('authors/', views.AuthorListView.as_view()),
  path('developers/', views.DeveloperListView.as_view()),
  path('ad/<int:pk>/', views.AdDetailView.as_view()),
  path('convenience/', views.СonvenienceCreateView.as_view())
]