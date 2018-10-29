from django.db import models
from datetime import datetime
# Create your models here.
class  IDCinfo(models.Model):
	"""机房管理"""
	idc_name = models.CharField(max_length=50, verbose_name='机房名称')
	idc_address = models.CharField(max_length=50, verbose_name='机房地址')
	idc_tag = models.CharField(max_length=50, verbose_name='机房标识符',unique=True)
	idc_leader = models.CharField(max_length=50, verbose_name='机房负责人')
	idc_leader_phone = models.CharField(max_length=50, verbose_name='机房负责人联系方式')
	idc_desc = models.CharField(max_length=50, verbose_name='备注')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	
	class  Meta:
		verbose_name = '机房管理'
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.idc_name
		
class  Serverinfo(models.Model):
	"""服务器机型"""
	server_category = models.CharField(max_length=50, verbose_name='机型',unique=True)
	server_product = models.CharField(max_length=50, verbose_name='品牌')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	server_config = models.CharField(max_length=220, verbose_name='配置',default="")
	server_desc = models.CharField(max_length=500, verbose_name='备注')
	class  Meta:
		verbose_name = '服务器机型'
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.server_category
	
class  Servefactoryrinfo(models.Model):
	"""供应商信息"""
	factory_name = models.CharField(max_length=50, verbose_name='供应商名称',unique=True)
	factory_address = models.CharField(max_length=50, verbose_name='公司地址')
	factory_category = models.IntegerField(choices=((0,'原厂商'),(1,'集成商')), default=1,verbose_name='厂商类型')
	factory_leader = models.CharField(max_length=50, verbose_name='项目负责人')
	factory_leader_phone = models.CharField(max_length=50, verbose_name='项目负责人联系方式')
	factory_desc = models.CharField(max_length=500, verbose_name='备注')
	factory_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	class  Meta:
		verbose_name = '供应商信息'
		verbose_name_plural = verbose_name
		ordering = ('factory_time',)
		
	def __str__(self):
		return self.factory_name
	
class  Application_info(models.Model):
	application_name = models.CharField(max_length=50, verbose_name='应用名称')
	application_tag  = models.CharField(max_length=50, verbose_name='应用标识符',unique=True)
	application_owner = models.CharField(max_length=50, verbose_name='应用负责人')
	application_department = models.CharField(max_length=50, verbose_name='应用部门')
	application_desc = models.CharField(max_length=500, verbose_name='应用简介')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	class  Meta:
		verbose_name = '应用类型'
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.application_tag