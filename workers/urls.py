from django.urls import path
from . import views

urlpatterns = [
  path('realtors/', views.RealtorListView.as_view()),
  path('positions/', views.PositionListView.as_view()),
  path('realtor/<int:pk>/', views.RealtorDetailView.as_view()),
]