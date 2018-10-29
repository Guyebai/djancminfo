from django.db import models
from  datetime import   datetime
from baseinfo.models import IDCinfo,Serverinfo,Servefactoryrinfo,Application_info


# Create your models here.
class  Trouble_type (models.Model):
	trouble_name = models.CharField(max_length=50, verbose_name='故障类型',unique=True,help_text='故障类型')
	trouble_desc = models.CharField(max_length=50, default="物理机硬件故障",verbose_name='故障描述',help_text='故障描述')
	trouble_influence = models.IntegerField(choices=((0,'不需要重启，不影响主机运行'),(1,'需要重启，影响主机运行')),verbose_name="是否影响主机",default=0,help_text='是否需要重启')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	
	class  Meta:
		verbose_name = '故障类型'
		verbose_name_plural = verbose_name
	
	def __str__(self):
		return self.trouble_name
class  Server_problem(models.Model):
	host_ip = models.CharField(max_length=50, verbose_name='主机IP')
	application_lines = models.ForeignKey(Application_info, verbose_name='应用名称',null=True, on_delete=models.CASCADE)
	host_sn = models.CharField(max_length=20, verbose_name='SN编号')
	factory_name = models.ForeignKey(Servefactoryrinfo, verbose_name='厂商',null=True, on_delete=models.CASCADE,related_name='factoryname')
	server_category = models.ForeignKey(Serverinfo, verbose_name='机型',null=True, on_delete=models.CASCADE)
	problem_time = models.DateTimeField(default=datetime.now, verbose_name='故障报修时间')
	repair_time =  models.DateTimeField(default=datetime.now, verbose_name='故障维修时间')
	trouble_name =  models.ForeignKey(Trouble_type, verbose_name='故障类型',null=True, on_delete=models.CASCADE,related_name='tracks')
	#trouble_influence = models.ForeignKey(Trouble_type, verbose_name='故障影响',null=True, on_delete=models.CASCADE)
	idc_name = models.ForeignKey(IDCinfo, verbose_name='所属机房',null=True, on_delete=models.CASCADE)
	problem_desc = models.CharField(max_length=50, verbose_name='更换备件')
	problem_info = models.CharField(max_length=50, verbose_name='备注')
	add_time =  models.DateTimeField(default=datetime.now, verbose_name='登记时间')
	class Meta:
		verbose_name = '服务器故障'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.host_ip
