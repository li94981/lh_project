from django.urls import path,include
from rotationapp import views
# 轮播图app
app_name = 'rotationapp'
urlpatterns = [
    path('tuichu/', views.tuichu,name='tuichu'),
    # 登录页面
    path('index/', views.index,name='index'),
    path('get_data/', views.get_data,name='get_data'),
    path('edit/', views.edit,name='edit'),
    path('add_banner/', views.add_banner,name='add_banner'),
    path('updateemp/', views.updateemp,name='updateemp'),
    path('deless/', views.deless,name='deless'),


]