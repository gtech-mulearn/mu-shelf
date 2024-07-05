from rest_framework.views import APIView
from utils.permission import JWTUtils
from .serializer import Problem_statement_serializer
from utils.response import CustomResponse
from .models import ProblemStatement, User
from utils.permission import CustomizePermission

class ProblemStatementAPI(APIView):
    permission_classes = [CustomizePermission]
    def get(self, request):
        serializer = Problem_statement_serializer(ProblemStatement.objects.all(), many=True)
        return CustomResponse(response=serializer.data).get_success_response()
    
    def post(self, request):
        user = User.objects.get(id=JWTUtils.fetch_user_id(request))
        serializer = Problem_statement_serializer(data=request.data)
        if not serializer.is_valid():
            return CustomResponse(message=serializer.errors).get_failure_response()
        serializer.save(created_by=user)
        return CustomResponse(general_message="Problem statement uploaded successfully").get_success_response()

class ProblemStatementDetailAPI(APIView):
    permission_classes = [CustomizePermission]

    def get(self, request, pk=None):
        problem_statement = ProblemStatement.objects.filter(id=pk).first()
        if not problem_statement:
            return CustomResponse(general_message="Problem Statement not found").get_failure_response()
        return CustomResponse(response=Problem_statement_serializer(problem_statement).data).get_success_response()
        
    def patch(self, request, pk=None):
        instance = ProblemStatement.objects.filter(id=pk).first()
        if not instance:
            return CustomResponse(general_message="Problem Statement not found").get_failure_response()
        serializer = Problem_statement_serializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return CustomResponse(general_message=serializer.errors).get_failure_response()
        serializer.save()
        return CustomResponse(general_message="Problem statement updated successfully").get_success_response()
    
    def delete(self, request, pk=None):
        instance = ProblemStatement.objects.filter(id=pk).first()
        if not instance:
            return CustomResponse(general_message="Problem Statement not found").get_failure_response()
        instance.delete()
        return CustomResponse(general_message="Problem statement deleted successfully").get_success_response()





class SolutionAPI(APIView):
    
    def get(self, request):
        pass
