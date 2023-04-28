from django.urls import path

from .views import *

urlpatterns = [
    #usuarios
    path('usuario/list/',UserListView.as_view(), name='user_list'),
    path('usuario/new/',UserCreateView.as_view(), name='user_new'),
    path('usuario/edit/<int:pk>',UserEditView.as_view(), name='user_edit'),
    path('usuario/del/<int:pk>',UsuarioDeleteView.as_view(), name='user_del'),
    path('usuario/ver/<int:pk>',UserDetalleView.as_view(), name='user_ver'),   
    path('profile/', UserPerfilView.as_view(), name='user_profile'),
    
    path('usuario/change/password/', PasswordChangeView.as_view(), name='user_change_pass'),
]