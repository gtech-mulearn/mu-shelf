from django.urls import path
from .company_view import CompanyProfileCreateAPI

urlpatterns = [
    path("profile/", CompanyProfileCreateAPI.as_view(), name="company_profile_create")
]
