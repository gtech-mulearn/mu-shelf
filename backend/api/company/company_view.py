from rest_framework.views import APIView
from .serializer import CompanyProfileSerializer
from utils.response import CustomResponse


class CompanyProfileCreateAPI(APIView):

    def post(self, request):
        data = request.data
        data['created_by'] = request.user.id
        serializer = CompanyProfileSerializer(data=data)
        if not serializer.is_valid():
            return CustomResponse(message=serializer.errors).get_failure_response()
        serializer.save()