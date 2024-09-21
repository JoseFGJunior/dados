from django.urls import path
from api import views

urlpatterns = [
    path ('',views.TenantListView.as_view(), name='tenant-list'),
    path ('create/',views.TenantCreateView.as_view(), name='tenant-create'),
    path ('update/<str:pk>/',views.TenantUpdateView.as_view(), name='tenant-update'),
    path ('delete/<str:pk>/',views.TenantDeleteView.as_view(), name='tenant-delete'),
    path ('<str:pk>/', views.TenantDetailView.as_view(), name='tenant-detail'),
    

]