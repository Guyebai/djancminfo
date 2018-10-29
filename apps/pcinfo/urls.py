from django.conf.urls import url, include
#from  troubleinfo import views
#from    import Trouble_type,Server_problem
from rest_framework import routers, serializers, viewsets
from .models import Pcinfo
from   baseinfo.pagination  import StandardResultsPagination

class PcinfoViewSet(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pcinfo
		fields = ('url', 'id','host_ip', 'server_category','idc_name','host_sn','host_number')
class PcserverinfoViewSet(viewsets.ModelViewSet):
	queryset = Pcinfo.objects.all()
	serializer_class = PcserverinfoSerializer
	pagination_class = StandardResultsPagination
	