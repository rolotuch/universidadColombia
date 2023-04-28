from django.urls import path
from .views import *

urlpatterns = [    
    path('pais/list/', PaisListView.as_view(), name='pais_list'),
    path('pais/alta/', PaisNew.as_view(), name='pais_new'),
    path('pais/update/<int:pk>', PaisEdit.as_view(), name='pais_edit'),
    path('pais/inactivar/<int:id>', pais_inactivar, name='pais_inactivar'),

    path('depto/list/', DepartamentoListView.as_view(), name='depto_list'),
    path('depto/alta/', DepartamentoNew.as_view(), name='depto_new'),
    path('depto/update/<int:pk>', DepartamentoEdit.as_view(), name='depto_edit'),
    path('depto/inactivar/<int:id>', depto_inactivar, name='depto_inactivar'),

    path('ciudad/list/', CiudadListView.as_view(), name='ciudad_list'),
    path('ciudad/alta/', CiudadNew.as_view(), name='ciudad_new'),
    path('ciudad/update/<int:pk>', CiudadEdit.as_view(), name='ciudad_edit'),
    path('ciudad/inactivar/<int:id>', ciudad_inactivar, name='ciudad_inactivar'),

    path('conocimiento/list/', ConocimientoListView.as_view(), name='cono_list'),
    path('conocimiento/alta/', ConocimientoNew.as_view(), name='cono_new'),
    path('conocimiento/update/<int:pk>', ConocimientoEdit.as_view(), name='cono_edit'),
    path('conocimiento/inactivar/<int:id>', cono_inactivar, name='cono_inactivar'),

    path('formacion/list/', FormacionListView.as_view(), name='form_list'),
    path('formacion/alta/', FormacionNew.as_view(), name='form_new'),
    path('formacion/update/<int:pk>', FormacionEdit.as_view(), name='form_edit'),
    path('formacion/inactivar/<int:id>', form_inactivar, name='form_inactivar'),

]