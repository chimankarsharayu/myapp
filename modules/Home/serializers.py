from rest_framework import serializers
from modules.Home.models import homeTable

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = homeTable
        fields = '__all__'