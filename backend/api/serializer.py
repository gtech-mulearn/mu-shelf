from rest_framework import serializers
from .models import ProblemStatement, Solution, Contributor
from django.db import transaction

class Problem_statement_serializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemStatement
        fields = ['id', 'title', 'description', 'reward', 'start', 'end', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['id', 'created_by']

    


class Contributor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["name", "email", "contact"]


class Solution_serializer(serializers.ModelSerializer):
    contributors = Contributor_serializer(many=True)
    class Meta:
        model = Solution
        fields = ['id', 'title', 'description', 'is_winner', 'problem_statement', 'created_at', 'created_by', 'updated_at', 'contributors']
        read_only_fields = ['is_winner', 'created_by']
    
    def create(self, validated_data):
        contributers_data = validated_data.pop("contributors")
        solution = Solution.objects.create(**validated_data)
        for contributer in contributers_data:
            Contributor.objects.create(solution=solution, **contributer)
        return solution
    
    def update(self, instance, validated_data):
        contributors_data = validated_data.pop("contributors", None)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        with transaction.atomic():
            instance.save()
            if contributors_data is not None:
                instance.contributors.all().delete()
                for contributor in contributors_data:
                    Contributor.objects.create(solution=instance, **contributor)
        return instance
    

class Problem_statement_detail_serializer(serializers.ModelSerializer):
    solutions = Solution_serializer(many=True, read_only=True)
    class Meta:
        model = ProblemStatement
        fields = ['id', 'title', 'description', 'reward', 'start', 'end', 'created_at', 'updated_at', 'created_by', 'approved', 'solutions',]