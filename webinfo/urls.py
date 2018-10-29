"""webinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from  extra_app import  xadmin
import webinfo.settings
from django.urls import path
from django.conf.urls import url, include

from django.views.generic import TemplateView #利用TemplateView
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from  rest_framework.documentation import include_docs_urls #文档
from rest_framework_jwt.views import obtain_jwt_token #jwt_token
from rest_framework_jwt.views import refresh_jwt_token

from  baseinfo.views import Application_infoViewSet,IDCinfoViewSet,ServefactoryrViewSet,ServerinfoViewSet
from  troubleinfo.views import TroubleViewSet,Server_problemViewSet
from  pcinfo.views  import  PcinfoViewSet

from  rest_framework.authtoken import  views

#userinfo
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
        #fields = ('url', 'username', 'email', 'is_staff')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'troubles', TroubleViewSet)#故障类型
router.register(r'problems', Server_problemViewSet)#故障登记
router.register(r'idcinfos', IDCinfoViewSet) #机房信息表
router.register(r'pcinfos', PcinfoViewSet) #服务器信息表
router.register(r'servefactoryrs', ServefactoryrViewSet)#厂商
router.register(r'applications', Application_infoViewSet)#应用
router.register(r'serverinfos', ServerinfoViewSet)#机型

urlpatterns = [
    url(r'^api/', include(router.urls)),
    path('xadmin/', xadmin.site.urls),
    path('admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name="index.html")),
    url(r'^docs/', include_docs_urls(title="cmdb")),
    # url(r'^', include('troubleinfo.urls')),
    url(r'^apiauth/', include('rest_framework.urls',namespace="rest_framework.urls")),
	
	#drf自带token认证模式
	url(r'^api-token/', views.obtain_auth_token),
    
    #jwt的认证接口
    url(r'^login/', obtain_jwt_token),
    
    #jwt 更新接口
    url(r'^api-token-refresh/', refresh_jwt_token),

]


