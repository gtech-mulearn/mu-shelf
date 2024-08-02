from rest_framework import serializers
from api.models import CompanyProfile

class CompanyProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyProfile
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'created_by']