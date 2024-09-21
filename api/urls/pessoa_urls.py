from django.urls import path
from api import views

urlpatterns = [
    path('',views.PessoaListView.as_view(), name='pessoa-list'),
    path('create/',views.PessoaCreatView.as_view(), name='pessoa-create'),
    path('update/<str:pk>/',views.PessoaUpdateView.as_view(), name='pessoa-update'),
    path('delete/<str:pk>/',views.PessoaDeleteView.as_view(), name='pessoa-delete'),
    path('<str:pk>/',views.PessoaDetailView.as_view(), name='pessoa-detail'),
   
    
]