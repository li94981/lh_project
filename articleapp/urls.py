from django.urls import path,include
from articleapp import views
# 文章管理app
app_name = 'articleapp'
urlpatterns = [
    #访问kindeditor测试页面
    path('kind/',views.kind,name='kind'),
    # 上传图片
    path('upload_img/', views.upload_img,name='upload_img'),
    # 获取所有曾经上传过的图片
    path('get_all_img/', views.get_all_img,name='get_all_img'),
    path('add_article/', views.add_article,name='add_article'),
    path('getALLArticle/', views.getALLArticle,name='getALLArticle'),
    path('deless/', views.deless,name='deless'),
    path('updateemp/', views.updateemp,name='updateemp'),



]