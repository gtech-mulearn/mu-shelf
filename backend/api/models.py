from django.db import models
import uuid


class ProblemStatement(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()
    reward = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)

    class Meta:
        managed = False
        db_table = 'problem_statement'

class Solution(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_winner = models.BooleanField(default=False)
    problem_statement = models.ForeignKey(ProblemStatement, related_name="solutions", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'solution'



class Contributors(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.TextField(null=True)
    solution = models.ForeignKey(Solution, related_name="contributors", on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'contributors'