import django_filters
from   .models import    Application_info

class ProductFilter(django_filters.FilterSet):
	application_name = django_filters.CharFilter(lookup_expr='iexact')
	application_tag = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model =  Application_info
        fields = ['application_name', 'application_name']