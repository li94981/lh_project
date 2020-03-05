from django.urls import path,include
from homeapp import views
# 主页app
app_name = 'homeapp'
urlpatterns = [
    # 主页面
    path('home/', views.home,name='home'),
    # 登录页面
    path('login_form/', views.login_form,name='login_form'),
    # 登录页面
    path('user_login/', views.user_login,name='user_login'),
    # 发送验证码
    path('get_code/', views.get_code,name='get_code'),

]