from django.urls import path
from .solution_view import SolutionUpdateDeleteAPI, SolutionPostAPI,SolutionWinner,SolutionTopRate

urlpatterns = [
    path("", SolutionPostAPI.as_view(), name="solution_create"),
    path("update/<str:pk>/", SolutionUpdateDeleteAPI.as_view(), name="solution_update"),
    path("winner/<str:pk>/", SolutionWinner.as_view(), name="solution_winner"),
    path("top-rate/<str:pk>/", SolutionTopRate.as_view(), name='solution_toprate')
]
