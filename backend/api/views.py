from rest_framework.views import APIView
from utils.permission import JWTUtils
from .serializer import Problem_statement_serializer
from utils.response import CustomResponse
from .models import ProblemStatement

class ProblemStatementAPI(APIView):
    # testing
    def get(self, request):
        serializer = Problem_statement_serializer(ProblemStatement.objects.all(), many=True)
        return CustomResponse(general_message=serializer.data).get_success_response()
    
    def post(self, request):
        serializer = Problem_statement_serializer(data=request.data)
        if not serializer.is_valid():
            return CustomResponse(message=serializer.errors).get_failure_response()
        serializer.save()

        return CustomResponse(message=serializer.data).get_success_response()




class SolutionAPI(APIView):
    
    def get(self, request):
        pass
