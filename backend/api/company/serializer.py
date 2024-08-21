from rest_framework import serializers
from api.models import CompanyProfile

class CompanyProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyProfile
        fields = ['email', 'organization', 'mobile', 'size', 'bio', 'website']

    def create(self, validated_data):
        user_id = self.context.get("user_id")
        validated_data['created_by_id'] = user_id
        return super().create(validated_data)