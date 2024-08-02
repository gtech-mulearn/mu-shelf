from rest_framework.views import APIView
from utils.permission import JWTUtils
from .serializer import Problem_statement_serializer, Problem_statement_detail_serializer
from utils.response import CustomResponse
from api.models import ProblemStatement, User
from utils.permission import CustomizePermission
from utils.utils import CommonUtils



class ProblemStatementPublicAPI(APIView):
    permission_classes = [CustomizePermission]
    def get(self, request):
        all_ps = ProblemStatement.objects.filter(approved=True)
        paginated_queryset = CommonUtils.get_paginated_queryset(
            all_ps, request, []
        )
        serializer = Problem_statement_serializer(paginated_queryset.get('queryset'), many=True)
        return CustomResponse().paginated_response(
            data=serializer.data,
            pagination=paginated_queryset.get('pagination')
        )

class ProblemStatementCreateAPI(APIView):
    def post(self, request):
        user = User.objects.get(id=JWTUtils.fetch_user_id(request))
        serializer = Problem_statement_serializer(data=request.data)
        if not serializer.is_valid():
            return CustomResponse(message=serializer.errors).get_failure_response()
        serializer.save(created_by=user)
        return CustomResponse(general_message="Problem statement uploaded successfully").get_success_response()


class ProblemStatementUpdateDeleteAPI(APIView):
    permission_classes = [CustomizePermission]
        
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

    def get(self, request, pk=None):
        if pk is None:
            user_id = JWTUtils.fetch_user_id(request)
            problem_statements = ProblemStatement.objects.filter(created_by=user_id)
        else:
            pass
        serializer = Problem_statement_detail_serializer(problem_statements, many=True)
        return CustomResponse(response=serializer.data).get_success_response()

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
    