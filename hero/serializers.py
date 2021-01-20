from rest_framework import serializers
from . models import Company, Employeer

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Company
        fields='__all__'
    
class EmployeerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Employeer
        fields='__all__'
    