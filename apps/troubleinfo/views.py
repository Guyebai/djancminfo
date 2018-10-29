from django.shortcuts import render
from  django.views.generic.base import    View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework
from rest_framework import filters
from rest_framework import routers, serializers, viewsets
from  .models  import Trouble_type,Server_problem
from  .serializers import Server_problemSerializer,TroubleSerializer
from   baseinfo.pagination  import StandardResultsPagination

class Server_problemViewSet(viewsets.ModelViewSet):
	"""故障主机信息接口"""
	queryset = Server_problem.objects.all()
	serializer_class = Server_problemSerializer
	http_method_names = ['get', 'post', 'patch', 'delete']
	pagination_class = StandardResultsPagination
	filter_backends = (filters.SearchFilter,)
	search_fields = ('host_ip',)
	

class TroubleViewSet(viewsets.ModelViewSet):
	"""故障类型信息接口"""
	queryset = Trouble_type.objects.all()
	serializer_class = TroubleSerializer
	http_method_names = ['get', 'post', 'patch', 'delete']
	pagination_class = StandardResultsPagination
	filter_backends = (filters.SearchFilter,)
	search_fields = ('trouble_name', 'trouble_desc')