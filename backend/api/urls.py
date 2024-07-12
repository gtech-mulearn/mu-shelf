from django.urls import path
from . import views

urlpatterns = [
    path('statement/', views.ProblemStatementAPI.as_view(), name="problem-statement"),
    path('statement/<str:pk>/', views.ProblemStatementDetailAPI.as_view(), name="problem-statement-detail"),
    path('statement-company/', views.ProblemStatementCompanyAPI.as_view(), name="problem-statement-company"),
    path('statement-approve/', views.ProblemStatementApproveAPI.as_view(), name="problem-statement-approve"),
    path('solution/', views.SolutionPostAPI.as_view(), name="solution-post"),
    path('solution/<str:pk>/', views.SolutionAPI.as_view(), name="solution"),
]