from django.db import models

class Tenant(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
     return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)  
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nome
    
     
    