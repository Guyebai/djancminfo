from django.shortcuts import render

# Create your views here.



from rest_framework import filters
from rest_framework import routers, serializers, viewsets

from  .models import  Application_info,Servefactoryrinfo,Serverinfo,IDCinfo

from  .serializers import  Application_infoSerializer,IDCinfoSerializer,ServefactoryrSerializer,ServerinfoSerializer
	#,,ServerinfoSerializer,IDCinfo
from baseinfo.pagination import StandardResultsPagination


class  Application_infoViewSet(viewsets.ModelViewSet):
	"""应用信息接口"""
	queryset = Application_info.objects.all()
	serializer_class =  Application_infoSerializer
	http_method_names = ['get', 'post', 'patch', 'delete']
	pagination_class = StandardResultsPagination
	filter_backends = (filters.SearchFilter,)
	search_fields = ('application_name',
	                 'application_tag',
	                 'application_owner',
	                 'application_department',
	                 'application_desc'
	                 )


# IDCinfo API

class IDCinfoViewSet(viewsets.ModelViewSet):
	"""机房信息接口"""
	queryset = IDCinfo.objects.all()
	serializer_class = IDCinfoSerializer
	pagination_class = StandardResultsPagination
	filter_backends = (filters.SearchFilter,)
	search_fields = ('idc_name',
	                 'idc_tag',
	                 'idc_leader',
	                 'idc_address',
	                 'idc_desc',
	                 'idc_leader_phone'
	                 )
	


class ServefactoryrViewSet(viewsets.ModelViewSet):
	"""供应商信息接口"""
	queryset = Servefactoryrinfo.objects.all()
	serializer_class = ServefactoryrSerializer
	pagination_class = StandardResultsPagination
	filter_backends = (filters.SearchFilter,)
	search_fields = ('factory_name',
	                 'factory_address',
	                 'factory_category',
	                 'factory_leader',
	                 'factory_leader_phone',
	                 'factory_desc'
	                 )




class ServerinfoViewSet(viewsets.ModelViewSet):
	"""机型信息接口"""
	queryset = Serverinfo.objects.all()
	serializer_class = ServerinfoSerializer
	pagination_class = StandardResultsPagination
	filter_backends = (filters.SearchFilter,)
	search_fields = (
			'server_category',
			'server_product',
			'server_config',
			'server_desc'
	                 )
	
