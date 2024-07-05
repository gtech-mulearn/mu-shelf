from django.urls import path
from . import views

urlpatterns = [
    path('statement/', views.ProblemStatementAPI.as_view(), name="problem-statement"),
    path('statement/<str:pk>/', views.ProblemStatementDetailAPI.as_view(), name="problem-statement-detail")
]