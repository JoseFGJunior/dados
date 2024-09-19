from django.contrib import admin
from .Models.sgd_models import Pessoa,Tenant

admin.site.register(Tenant)
admin.site.register(Pessoa)
'''

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
 list_display = ('nome','tenant')
 list_filter = ('nome','tenant')
 search_fields = ('nome','tenant')

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
 list_display = ('Nome','descricao')
 list_filter = ('nome','descricao')
 search_fields = ('nome','descricao')
'''

