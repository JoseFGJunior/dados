from django.urls import path
from api import views


urlpatterns = [
    path ('',       views.TenantListView.as_view(), name='tenant-list'),
    path ('create/',views.TenantCreateView.as_view(), name='tenant-create'),
    
]