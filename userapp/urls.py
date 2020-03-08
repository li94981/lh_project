from django.urls import path,include
from userapp import views
# 用户管理app
app_name = 'userapp'
urlpatterns = [
    path("edit2/", views.edit2, name='edit2'),
    path("get_data2/", views.get_data2, name='get_data2'),
    path("qushi/", views.qushi, name='qushi'),
    path("get_map/", views.get_map, name='get_map'),

]