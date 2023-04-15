from rest_framework import serializers

from . import models

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()
    # max_length=255

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = ["id", "name", "description", "salary", "company"]