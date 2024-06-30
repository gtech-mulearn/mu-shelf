from django.db import models
import uuid
from .managers import user_manager
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from decouple import config as decouple_config

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    discord_id = models.CharField(unique=True, max_length=36, blank=True, null=True)
    muid = models.CharField(unique=True, max_length=100)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=200)
    password = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(unique=True, max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=[("Male", "Male"), ("Female", "Female")])
    dob = models.DateField(blank=True, null=True)
    admin = models.BooleanField(default=False)
    exist_in_guild = models.BooleanField(default=False)
    district = models.ForeignKey("District", on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    suspended_at = models.DateTimeField(blank=True, null=True)
    suspended_by = models.ForeignKey("self", on_delete=models.SET(settings.SYSTEM_ADMIN_ID), blank=True, null=True,
                                     related_name="user_suspended_by_user", db_column="suspended_by", default=None)
    objects = user_manager.ActiveUserManager()
    every = models.Manager()

    class Meta:
        managed = False
        db_table = 'user'

    @property
    def profile_pic(self):
        fs = FileSystemStorage()
        path = f'user/profile/{self.id}.png'
        if fs.exists(path):
            return f"{decouple_config('BE_DOMAIN_NAME')}{fs.url(path)}"

    def save(self, *args, **kwargs):
        if self.muid is None:
            full_name = self.full_name.replace(" ", "-").lower()
            self.muid = f"{full_name}@mulearn"

            counter = 0
            while User.objects.filter(muid=self.muid).exists():
                counter += 1
                self.muid = f"{full_name}-{counter}@mulearn"

        return super().save(*args, **kwargs)


class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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