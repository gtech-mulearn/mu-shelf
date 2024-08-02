from api.models import ProblemStatement
from rest_framework import serializers
from api.solution.serializer import Solution_serializer

class Problem_statement_serializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemStatement
        fields = ['id', 'title', 'description', 'reward', 'start', 'end', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['id', 'created_by']

class Problem_statement_detail_serializer(serializers.ModelSerializer):
    solutions = Solution_serializer(many=True, read_only=True)
    class Meta:
        model = ProblemStatement
        fields = ['id', 'title', 'description', 'reward', 'start', 'end', 'created_at', 'updated_at', 'created_by', 'approved', 'solutions',]