from django.urls import path, include

urlpatterns = [
    path("problem-statement/", include("api.problem_statement.urls")),
    path("solution/", include("api.solution.urls")),
    path("company/", include("api.company.urls")),
]