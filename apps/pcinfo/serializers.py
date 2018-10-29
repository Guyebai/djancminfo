from rest_framework import serializers
from  .models  import  Pcinfo

class PcinfoSerializer(serializers.HyperlinkedModelSerializer):
	"""主机序列化"""
	class Meta:
		model = Pcinfo
		fields = ('host_ip',
		          'host_sn',
		          'host_cabinet',
		          'host_number',
		          'host_info',
		          'factory_name',
		          'idc_name',
		          'server_category'
		          )


