from django.urls import path,include
from rotationapp import views
# 轮播图app
app_name = 'rotationapp'
urlpatterns = [
    # 退出登录状态
    path('tuichu/', views.tuichu,name='tuichu'),
    # 登录状态判断逻辑
    path('index/', views.index,name='index'),
    # 返回用户所需json数据
    path('get_data/', views.get_data,name='get_data'),
    # 编辑用户逻辑实现
    path('edit/', views.edit,name='edit'),
    # 添加用户逻辑实现
    path('add_banner/', views.add_banner,name='add_banner'),
    # 修改用户逻辑实现
    path('updateemp/', views.updateemp,name='updateemp'),
    # 删除用户逻辑实现
    path('deless/', views.deless,name='deless'),


]