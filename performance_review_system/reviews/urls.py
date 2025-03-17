from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_review, name='add_review'),
    path('', views.review_list, name='review_list'),
    path('review/<int:id>/edit/', views.edit_review, name='edit_review'),  # Edit review
    path('review/<int:id>/delete/', views.delete_review, name='delete_review'),  # Delete review
    path('review/<int:id>/', views.review_detail, name='review_detail'),
   ]
