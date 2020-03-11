import json

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from mutagen.mp3 import MP3

from albumapp.models import Album, Chapter


def getAllAlbum(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    album = Album.objects.all().order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)

    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, Album):
            return {
                "author": u.author,
                "brief": u.brief,
                "broadcast": u.broadcast,
                "count": u.count,
                "cover": u.cover,
                "createDate": u.create_date,
                "id": u.id,
                "publishDate": u.publish_date,
                "score": u.score,
                "status": u.status,
                "title": u.title,
            }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)



def getChapterByAlbumId(request):
    album_Id = request.GET.get('albumId')
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    album = Chapter.objects.all().filter(album_id=album_Id).order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)

    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, Chapter):
            return {
                "albumId": u.album_id,
                "createDate": u.create_date.strftime("%Y-%m-%d"),
                "duration": u.duration,
                "id": u.id,
                "size": u.size,
                "title": u.title,
                "url": u.url,
            }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)
def getChapter(request):
    val = Chapter.objects.all().values()
    json_str = json.dumps(list(val))
    return HttpResponse(json_str)
def addalbum(request):
    title = request.GET.get("title")
    score = request.GET.get("score")
    author = request.GET.get("author")
    broadcast = request.GET.get("broadcast")
    count = request.GET.get("count")
    brief = request.GET.get("brief")
    publish_date = request.GET.get("publish_date")
    cover = request.GET.get("cover")
    status = request.GET.get("state")
    create_date = request.GET.get("create_date")
    print(title,status,score,publish_date)
    Album.objects.create(title=title, score=score, author=author, create_date=create_date,
                           publish_date=publish_date,broadcast=broadcast,count=count,
                         brief=brief,cover=cover,status=status)
    return HttpResponse('OK')

def delete(request):
    id = request.GET.get('id')
    print(id)
    Id = Album.objects.filter(id=id)
    if Id:
        Id.delete()
        return JsonResponse({"error": "0"})
    else:
        return JsonResponse({"error": 1, "msg": "删除失败！"})
def updata(request):
    pass