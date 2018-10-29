from django.db import models

from datetime import datetime
from baseinfo.models import IDCinfo,Serverinfo,Servefactoryrinfo
# Create your models here.
class Pcinfo(models.Model):
	host_ip = models.CharField(max_length=40, verbose_name='主机IP',unique=True)
	host_sn = models.CharField(max_length=20, verbose_name='SN编号',unique=True)
	server_category = models.ForeignKey(Servefactoryrinfo, verbose_name='厂商',null=True, on_delete=models.CASCADE)
	#host_product = models.CharField(max_length=500, verbose_name='厂商名称')
	factory_name =models.ForeignKey(Serverinfo, verbose_name='机型',null=True, on_delete=models.CASCADE)
	idc_name = models.ForeignKey(IDCinfo, verbose_name='所属机房',null=True, on_delete=models.CASCADE)
	#business_unit = models.ForeignKey('BusinessUnit', verbose_name=u'属于的业务线', null=True, blank=True)
	#host_room = models.CharField(default="下沙机房",max_length=500, verbose_name='机房')
	host_cabinet =models.CharField(default="F05-B12",max_length=500, verbose_name='机柜')
	host_number  =models.IntegerField(default=0,verbose_name='U位')
	host_info = models.CharField(max_length=500, verbose_name='配置')
	#update_time = models.DateTimeField(default=datetime.now, verbose_name='更改时间')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	
	class Meta:
		verbose_name = '主机信息'
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.host_ip
	
	
