from rest_framework.views import APIView
from .serializer import CompanyProfileSerializer
from utils.response import CustomResponse
from utils.permission import role_required, CustomizePermission, JWTUtils
from utils.types import RoleType
from api.models import UserOrganizationLink, CompanyProfile, Organization
from django.db.models import Count
from utils.utils import CommonUtils

class CompanyProfileCreateAPI(APIView):
    permission_classes = [CustomizePermission]

    @role_required([RoleType.COMPANY_MEMBER.value])
    def get(self, request):
        user_id = JWTUtils.fetch_user_id(request)
        organization = CommonUtils.get_organization(user_id)
        serializer = CompanyProfileSerializer(organization.company_profile)
        return CustomResponse(serializer.data).get_success_response()

    @role_required([RoleType.COMPANY_MEMBER.value])
    def post(self, request):
        data = request.data
        user_id = JWTUtils.fetch_user_id(request)
        serializer = CompanyProfileSerializer(data=data, context={"user_id": user_id})
        if not serializer.is_valid():
            return CustomResponse(message=serializer.errors).get_failure_response()
        serializer.save()
        return CustomResponse(general_message="Successfully created company profile").get_success_response()
    
    @role_required([RoleType.COMPANY_MEMBER.value])
    def patch(self, request):
        data = request.data
        user_id = JWTUtils.fetch_user_id(request)
        profile = UserOrganizationLink.objects.filter(user__id=user_id).first().org.company_profile
        serializer = CompanyProfileSerializer(profile, data=data, partial=True)
        if not serializer.is_valid():
            return CustomResponse(message=serializer.errors).get_failure_response()
        serializer.save()
        return CustomResponse(general_message="Successfylly updated company profile").get_success_response()
    
class CompanyProfilePublicAPI(APIView):
    permission_classes = [CustomizePermission]
    
    def get(self, request, pk=None):
        try:
            profile = CompanyProfile.objects.get(organization__id=pk)
            if profile is None:
                return CustomResponse(general_message="Organization not found").get_failure_response()
            serializer = CompanyProfileSerializer(profile)
            return CustomResponse(serializer.data).get_success_response()
        except CompanyProfile.DoesNotExist:
            return CustomResponse(general_message="Organization has no profile").get_failure_response()
    
class CompanyDashboardAPI(APIView):
    permission_classes = [CustomizePermission]

    def get(self, request):
        user_id = JWTUtils.fetch_user_id(request)
        user_organization = CommonUtils.get_organization(user_id)
        dashboard_data = Organization.objects.filter(id=user_organization.id).aggregate(problem_count=Count('problem_statements'), submission_count=Count('submissions'))
        return CustomResponse(dashboard_data).get_success_response()
