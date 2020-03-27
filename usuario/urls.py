from django.urls import path
from usuario import views
from usuario.views import mas_datos

urlpatterns = [
    path('nuevo/', views.usuario_create.as_view(), name='usuario_nuevo'),
    path('listar/', views.usuario_list.as_view(), name='usuario_listar'),
    path('editar/<pk>/',views.usuario_edit.as_view(), name='usuario_editar'),
    path('carga/<pk>/', views.carga_edit.as_view(), name='carga_editar'),
    path('buscar/', views.usuario_search, name='usuario_buscar'),
    path('mas_dato/<str:id_usuario>/', mas_datos.as_view(), name='mas_datos'),
]