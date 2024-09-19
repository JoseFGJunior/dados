from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from api.Models.sgd_models import Tenant,Pessoa
from api.serializers.sgd_serializers import PessoaSerializer,TenantSerializer


class PessoaListView(ListAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaDetailView(RetrieveAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    
class PessoaCreatView(CreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    
class PessoaUpdateView(UpdateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    
class PessoaDeleteView(DestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    
#-----Tenant -----# 
    
class TenantListView(ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantCreateView(CreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantUpodateView(UpdateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantDeleteView(DestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    
class TenantDetailView(RetrieveAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
