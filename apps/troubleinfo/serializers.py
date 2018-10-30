from  .models  import Trouble_type,Server_problem
from rest_framework import  serializers

from  .models  import Trouble_type,Server_problem

#故障主机序列化
class Server_problemSerializer(serializers.HyperlinkedModelSerializer):
	idc_name = serializers.ReadOnlyField(source='idc_name.idc_name')
	#tracks = serializers.StringRelatedField(many=True)
	trouble_name = serializers.ReadOnlyField(source='trouble_name.trouble_name')
	server_category = serializers.ReadOnlyField(source='server_category.server_category')
	factory_names = serializers.ReadOnlyField(source='factory_name.factory_name')
	
	class Meta:
		model = Server_problem
		fields = ('url',
		          'id',
		          'host_ip',
		          'host_sn',
		          'idc_name',
		          'trouble_name',
		          'problem_time',
		          'repair_time',
		          'problem_desc',
		          'server_category',
		          'problem_info',
		          'factory_names',
		          'factory_name',
		          )
		


		
#故障类型序列化
class TroubleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Trouble_type
		fields = ('url', 'id', 'trouble_name', 'trouble_desc','trouble_influence')