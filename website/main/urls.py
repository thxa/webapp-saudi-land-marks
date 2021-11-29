from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index),
    path("landmarks/<int:landmark_id>/", views.landmark),
    path("goals/", views.goals),
    path("rules/", views.rules),
    path("about/", views.about),
]
