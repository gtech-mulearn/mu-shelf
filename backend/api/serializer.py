from rest_framework import serializers
from .models import ProblemStatement

class Problem_statement_serializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemStatement
        fields = ['id', 'title', 'description', 'reward', 'start', 'end', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['id', 'created_by']