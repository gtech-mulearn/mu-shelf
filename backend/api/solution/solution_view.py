from rest_framework.views import APIView
from utils.permission import JWTUtils
from .serializer import Solution_serializer
from utils.response import CustomResponse
from api.models import User, Solution
from utils.permission import CustomizePermission
from utils.utils import CommonUtils


class SolutionPostAPI(APIView):
    permission_classes = [CustomizePermission]

    def post(self, request):
        user = User.objects.get(id=JWTUtils.fetch_user_id(request))
        serializer = Solution_serializer(data=request.data)
        if not serializer.is_valid():
            return CustomResponse(message=serializer.errors).get_failure_response()
        serializer.save(created_by=user)
        return CustomResponse(general_message="Solution uploaded successfully").get_success_response()

class SolutionUpdateDeleteAPI(APIView):
    permission_classes = [CustomizePermission]

    def delete(self, request, pk=None):
        instance = Solution.objects.filter(id=pk).first()
        if not instance:
            return CustomResponse(general_message="Solution not found").get_failure_response()
        instance.delete()
        return CustomResponse(general_message="Solution deleted successfully").get_success_response()
    
    def patch(self, request, pk=None):
        instance = Solution.objects.filter(id=pk).first()
        if not instance:
            return CustomResponse(general_message="Solution not found").get_failure_response()
        serializer = Solution_serializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return CustomResponse(general_message=serializer.errors).get_failure_response()
        serializer.save()
        return CustomResponse(general_message="Solution updated successfully").get_success_response()
        