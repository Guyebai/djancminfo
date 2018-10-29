from django.shortcuts import render

# Create your views here.
from rest_framework import filters
from rest_framework import routers, serializers, viewsets
from .models import  Pcinfo

from  .serializers import  PcinfoSerializer
from baseinfo.pagination import StandardResultsPagination


class PcinfoViewSet(viewsets.ModelViewSet):
	"""服务器信息信息接口"""
	queryset = Pcinfo.objects.all()
	serializer_class = PcinfoSerializer
	http_method_names = ['get', 'post', 'patch', 'delete']
	pagination_class = StandardResultsPagination
	filter_backends = (filters.SearchFilter,)
	search_fields = ('host_ip','host_sn','factory_name')


