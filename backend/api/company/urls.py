from django.urls import path
from .company_view import CompanyProfileCreateAPI, CompanyProfilePublicAPI, CompanyDashboardAPI

urlpatterns = [
    path("profile/", CompanyProfileCreateAPI.as_view(), name="company_profile_create"),
    path("profile/<str:pk>/", CompanyProfilePublicAPI.as_view(), name="company_profile_get_update"),
    path("dashboard/", CompanyDashboardAPI.as_view(), name="company_dashboard"),
]
