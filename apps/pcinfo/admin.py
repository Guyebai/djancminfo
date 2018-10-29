from django.contrib import admin
from   .models import Pcinfo

# Register your models here.
admin.site.site_header = '硬件管理系统'
admin.site.site_title = 'DBMS'

class PcinfoAdmin(admin.ModelAdmin):
	list_display = ['id','host_ip', 'idc_name','server_category','host_sn','host_cabinet','host_number','factory_name','add_time']
	#search_fileds
	search_fields = ['host_ip','host_sn']
admin.site.register(Pcinfo,PcinfoAdmin)