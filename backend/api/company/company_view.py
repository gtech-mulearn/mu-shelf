from rest_framework.views import APIView
from .serializer import CompanyProfileSerializer
from utils.response import CustomResponse
from utils.permission import role_required, CustomizePermission, JWTUtils
from utils.types import RoleType

class CompanyProfileCreateAPI(APIView):
    permission_classes = [CustomizePermission]

    @role_required([RoleType.COMPANY_MEMBER.value])
    def post(self, request):
        data = request.data
        user_id = JWTUtils.fetch_user_id(request)
        serializer = CompanyProfileSerializer(data=data, context={"user_id": user_id})
        if not serializer.is_valid():
            return CustomResponse(message=serializer.errors).get_failure_response()
        serializer.save()
        return CustomResponse(general_message="Successfully created company profile")