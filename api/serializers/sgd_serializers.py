from rest_framework import serializers
from api.Models.sgd_models import Tenant,Pessoa

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant  
        fields = '__all__'
        
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
        
        
   