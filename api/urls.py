from django.urls import path
from . import views

urlpatterns = [
    path('car', views.add_car),
    path('car/draft', views.draft_car)
]