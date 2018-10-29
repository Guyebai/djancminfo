from extra_app import  xadmin
from xadmin import views
class BaseSetting:
    '''
    增加主题样式
    '''
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    '''
    修改标题

    '''
    site_title = "jeff后台管理系统"
    site_footer = "http://www.cnblogs.com/Jeffding/"
    menu_style = "accordion"#下拉框收起来

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
