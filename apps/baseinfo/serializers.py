from rest_framework import serializers

from  .models import  Application_info,IDCinfo,Servefactoryrinfo,Serverinfo,Product_lines



class Application_infoSerializer(serializers.ModelSerializer):
	"""应用信息序列化"""
	
	line_idname = serializers.ReadOnlyField(source='line_name.line_name')
	
	class Meta:
		model = Application_info
		fields = (
			      'id',
				  'application_name',
		          'application_tag',
			      'line_name',
		          'application_owner',
		          'application_department',
		          'application_desc',
				   'line_idname',
		          )
		
class  IDCinfoSerializer(serializers.HyperlinkedModelSerializer):
	"""IDC机房信息序列化"""
	class Meta:
		model =IDCinfo
		fields =('url',
                 'id',
		         'idc_name',
                 'idc_address',
                 'idc_tag',
                 'idc_leader',
                 'idc_leader_phone','idc_desc',
                 )
        
        
#厂商信息接口Servefactoryrinfo
class  ServefactoryrSerializer(serializers.HyperlinkedModelSerializer):
	"""供应商信息序列化"""
	class Meta:
		model =Servefactoryrinfo
		fields =('url',
		         'id',
                 'factory_name',
                 'factory_address',
                 'factory_category',
                 'factory_leader',
                 'factory_leader_phone',
		         'factory_desc',
                 )

class ServerinfoSerializer(serializers.HyperlinkedModelSerializer):
	"""机型序列化"""
	
	class Meta:
		model = Serverinfo
		fields = (
			'id',
			'server_category',
			'server_product',
			'server_config',
			'server_desc'
		)


class ProductlinesSerializer(serializers.HyperlinkedModelSerializer):
	"""产品线序列化"""
	
	class Meta:
		model = Product_lines
		fields = (
			'id',
			'line_name',
			'line_tag',
			'line_owner',
			'line_department',
			'line_desc',
			
		)
