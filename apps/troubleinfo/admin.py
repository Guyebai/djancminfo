from django.contrib import admin
from  .models import   Trouble_type,Server_problem

# Register your models here.
class  Trouble_typeAdmin(admin.ModelAdmin):
	list_display = ['id','trouble_name','trouble_influence','add_time']
	search_fields = ['trouble_name','trouble_influence']
admin.site.register(Trouble_type,Trouble_typeAdmin)


class  Server_problemAdmin(admin.ModelAdmin):
	list_display = ['id', 'host_ip', 'application_lines', 'host_sn', 'factory_name', 'server_category', 'trouble_name',
	                'idc_name', 'problem_time', 'repair_time', 'problem_desc', 'add_time']
	search_fields = ['id', 'host_ip', 'application_lines', 'host_sn', 'factory_name', 'server_category', 'trouble_name',
	                 'idc_name']
admin.site.register(Server_problem,Server_problemAdmin)

