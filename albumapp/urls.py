from django.urls import path
from albumapp import views
app_name = 'albumapp'
urlpatterns = [
    # path("getAllAlbum/",views.getAllAlbum,name ='getAllAlbum'),
    path('getAllAlbum/', views.getAllAlbum,name='getAllAlbum'),
    path('getChapter/', views.getChapterByAlbumId,name='getChapterByAlbumId'),
    path('getChapter/', views.getChapter,name='getChapter'),
    path('addalbum/', views.addalbum,name='addalbum'),
    path('delete/', views.delete,name='delete'),
    path('delete/', views.updata(),name='delete'),
]