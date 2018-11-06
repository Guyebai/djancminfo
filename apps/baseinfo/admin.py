from django.contrib import admin

# Register your models here.

from  .models import IDCinfo,Serverinfo,Servefactoryrinfo,Application_info,Product_lines

# Register your models here.


class IDCinfoAdmin(admin.ModelAdmin):
	list_display = ['id','idc_name', 'idc_address','idc_tag','idc_leader','idc_leader_phone','idc_desc','add_time']
	search_fields = [ 'idc_address','idc_tag']
	list_filter = [ 'idc_address','idc_tag','idc_leader','idc_leader_phone','idc_desc']
admin.site.register(IDCinfo,IDCinfoAdmin)


class ServerinfoAdmin(admin.ModelAdmin):
	
	list_display = ['id','server_category', 'server_product','server_desc','add_time']
	search_fields = ['server_category', 'server_product','server_desc']
	list_filter = ['server_category', 'server_product','server_desc','add_time']
admin.site.register(Serverinfo,ServerinfoAdmin)


class ServefactoryrinfoAdmin(admin.ModelAdmin):
	list_display = ['id', 'factory_name', 'factory_address', 'factory_category', 'factory_leader','factory_leader_phone']
	search_fields = ['id', 'factory_name', 'factory_address', 'factory_category', 'factory_leader','factory_leader_phone']
admin.site.register(Servefactoryrinfo,ServefactoryrinfoAdmin)


#admin.site.register(Application_info) 简单注册




class ApplicationinfoAdmin(admin.ModelAdmin):
	list_display = [
		'application_name',
		'application_tag',
		'line_name',
		'application_owner',
		'application_department',
		'application_desc',
		
	]
	search_fields =[
		'application_name',
		'application_tag',
		'line_name',
		'application_owner',
		'application_department',
		'application_desc',
		
	]

admin.site.register(Application_info,ApplicationinfoAdmin)

class ProductlinesAdmin(admin.ModelAdmin):
	list_display = [
		'line_name',
		'line_tag',
		'line_owner',
		'line_department',
		'line_desc',
		'add_time',
		
	]
	search_fields = [
		'line_name',
		'line_tag',
		'line_owner',
		'line_department',
		'line_desc',

		]
admin.site.register(Product_lines,ProductlinesAdmin)


