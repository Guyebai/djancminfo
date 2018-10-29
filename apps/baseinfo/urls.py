from django.conf.urls import url, include
from  troubleinfo import views
from rest_framework import routers, serializers, viewsets
from .models  import   IDCinfo,Serverinfo,Servefactoryrinfo,Application_info
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework  import   filters
from   baseinfo.pagination  import StandardResultsPagination
import django_filters




    


