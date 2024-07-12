from rest_framework.views import APIView
from utils.permission import JWTUtils
from .serializer import Problem_statement_serializer, Solution_serializer, Problem_statement_detail_serializer
from utils.response import CustomResponse
from .models import ProblemStatement, User, Solution
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
        return CustomResponse(response=Problem_statement_detail_serializer(problem_statement).data).get_success_response()
        
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


class ProblemStatementCompanyAPI(APIView):
    permission_classes = [CustomizePermission]

    def get(self, request):
        user_id = JWTUtils.fetch_user_id(request)
        problem_statements = ProblemStatement.objects.filter(created_by=user_id)
        serializer = Problem_statement_detail_serializer(problem_statements, many=True)
        return CustomResponse(response=serializer.data).get_success_response()



class SolutionPostAPI(APIView):
    permission_classes = [CustomizePermission]

    def post(self, request):
        user = User.objects.get(id=JWTUtils.fetch_user_id(request))
        serializer = Solution_serializer(data=request.data)
        if not serializer.is_valid():
            return CustomResponse(message=serializer.errors).get_failure_response()
        serializer.save(created_by=user)
        return CustomResponse(general_message="Solution uploaded successfully").get_success_response()

class SolutionAPI(APIView):
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
        
    

class ProblemStatementApproveAPI(APIView):
    permission_classes = [CustomizePermission]

    def post(self, request):
        problem_statement_id = request.data.get('id')
        problem_statement = ProblemStatement.objects.filter(id=problem_statement_id).first()
        if not problem_statement:
            return CustomResponse(general_message="Problem statement not found").get_failure_response()
        problem_statement.approved = True
        problem_statement.save()
        return CustomResponse(general_message="Problem statement approved successfully").get_success_response()