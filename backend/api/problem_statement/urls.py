from django.urls import path
from .problem_statement_view import ProblemStatementPublicAPI, ProblemStatementUpdateDeleteAPI, ProblemStatementApproveAPI, ProblemStatementCompanyAPI, ProblemStatementCreateAPI

urlpatterns = [
    path("", ProblemStatementCreateAPI.as_view(), name="problem_statement_create"),
    path("list/", ProblemStatementPublicAPI.as_view(), name="problem_statement_list"),
    path("update/<str:pk>/", ProblemStatementUpdateDeleteAPI.as_view(), name="problem_statement_update_delete"),
    path("approve/", ProblemStatementApproveAPI.as_view(), name="problem_statement_approve"),
    path("company/<str:pk>", ProblemStatementCompanyAPI.as_view(), name="problem_statement_company"),
]
