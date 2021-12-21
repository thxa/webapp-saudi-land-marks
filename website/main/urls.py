from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index),
    path("landmarks/create/", views.landmark_create),
    path("landmarks/<int:landmark_id>/", views.landmark),
    path("landmarks/<int:landmark_id>/update/", views.landmark_update),
    path("landmarks/<int:landmark_id>/delete/", views.landmark_delete),
    path("goals/", views.goals),
    path("rules/", views.rules),
    path("about/", views.about),
]
