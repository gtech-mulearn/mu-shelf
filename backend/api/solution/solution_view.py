from rest_framework.views import APIView
from utils.permission import JWTUtils
from .serializer import Solution_serializer
from utils.response import CustomResponse
from api.models import User, Solution
from utils.permission import CustomizePermission,role_required
from utils.utils import CommonUtils
from utils.types import RoleType,WinnerType


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
        
class SolutionWinner(APIView):
    permission_classes = [CustomizePermission]
    
    @role_required([RoleType.COMPANY_MEMBER.value,RoleType.ADMIN.value])
    def patch(self, request, pk=None):
        new_status = request.data.get('winner_status')
        
        if new_status not in [tag.name for tag in WinnerType]:
            return CustomResponse(general_message="Invalid winner status").get_failure_response()

        instance = Solution.objects.filter(id=pk).first()
        if not instance:
            return CustomResponse(general_message="Solution not found").get_failure_response()
        
        instance.winner_status = new_status
        instance.save()
        return CustomResponse(general_message="Solution winner status changed successfully").get_success_response()
    
class SolutionTopRate(APIView):
    
    permission_classes = [CustomizePermission]
    
    @role_required([RoleType.COMPANY_MEMBER.value,RoleType.ADMIN.value])
    def patch(self, request, pk=None):
        instance = Solution.objects.filter(id=pk).first()
        if not instance:
            return CustomResponse(general_message="Solution not found").get_failure_response()
        
        instance.is_sorted = not instance.is_sorted
        instance.save()
        return CustomResponse(general_message="Solution top rated status changed successfully").get_success_response()