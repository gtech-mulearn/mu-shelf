from django.urls import path
from .solution_view import SolutionUpdateDeleteAPI, SolutionPostAPI

urlpatterns = [
    path("", SolutionPostAPI.as_view(), name="solution_create"),
    path("update/<str:pk>/", SolutionUpdateDeleteAPI.as_view(), name="solution_update"),
]
