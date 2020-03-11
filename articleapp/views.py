import json
import os
import datetime
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt

from articleapp.models import Pic,Mrticle


def getALLArticle(request):
    # page_num = request.GET.get('page')
    # row_num = request.GET.get('rows')
    #
    # rows = []
    # article = Mrticle.objects.all().order_by('id')
    # all_page = Paginator(article, row_num)
    # page = Paginator(article, row_num).page(page_num).object_list
    #
    # page_data = {
    #     "total": all_page.num_pages,
    #     "records": all_page.count,
    #     "page": page_num,
    #     "rows": rows
    # }
    #
    # for i in page:
    #     rows.append(i)
    #
    # def myDefault(u):
    #     if isinstance(u, Mrticle):
    #         return {'id': u.id,
    #                 'content': u.content,
    #                 'title': u.title,
    #                 'status': u.status,
    #                 'createDate': u.create_date.strftime('%Y-%m-%d'),
    #                 'publishDate': u.publish_date.strftime('%Y-%m-%d'),
    #                 }
    #
    # data = json.dumps(page_data, default=myDefault)
    #
    # return HttpResponse(data)
    val=Mrticle.objects.all().values()
    json_str=json.dumps(list(val))
    return HttpResponse(json_str)


# 访问kindeditor测试页面
def kind(request):
    return render(request, "kindeditor_test.html")


@xframe_options_sameorigin
@csrf_exempt
def upload_img(request):
    """
    完成富文本编辑器图片上传的功能
    :param request:
    :return:
    """
    # 获取页面imgFile
    image = request.FILES.get('imgFile')
    time = datetime.datetime.now()
    if image:
        img_url = request.scheme + "://" + request.get_host() + "/static/img/" + str(image)
        print(img_url)
        result = {"error": 0, "url": img_url}
        Pic.objects.create(img=image,upload_time=time)
    else:
        result = {"error": 0, "message": "上传出错"}

    return JsonResponse(result)


def get_all_img(request):
    """
    获取所有层上传过得图片
    :param request:
    :return: 所有图片以及对应的参数
    """
    # 找到图片所在的路径  方便回显
    pic_url = request.scheme + "://" + request.get_host() + "/"
    # 获取所有曾上传过得图片
    pic_all = Pic.objects.all()

    rows = []

    for pic in list(pic_all):
        # 获取图片后缀名
        path, pic_suffix = os.path.splitext(pic.img.url)
        rows.append({
            "is_dir": False,
            "has_file": False,
            "filesize": pic.img.size,
            "dir_path": "",
            "is_photo": True,
            "filetype": pic_suffix,
            "filename": pic.img.name,
            "datetime": pic.upload_time,
        })
    # 图片空间所需的所有数据
    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": pic_url,
        "total_count": len(pic_all),
        "file_list": rows
    }

    return JsonResponse(data)


def add_article(request):

    """
    完成添加文章的方法
    :param request:
    :return:
    """
    title = request.GET.get("title")
    status = request.GET.get("status")
    content = request.GET.get("content")
    create_date = datetime.datetime.now().strftime('%Y-%m-%d')
    publish_date = datetime.datetime.now().strftime('%Y-%m-%d')
    Mrticle.objects.create(title=title,status=status,content=content,create_date=create_date,publish_date=publish_date)
    return HttpResponse('OK')
    # if shuju:
    #     return JsonResponse({'state': 0, 'info': '数据保存成功'})
    # else:
    #     return JsonResponse({'state': 1, 'info': '数据保存失败'})
def updateemp(request):
    id = request.GET.get("id")
    title = request.GET.get("title")
    status = request.GET.get("status")
    content = request.GET.get("content")
    print(content,"hahahah",id)
    create_date = datetime.datetime.now().strftime('%Y-%m-%d')
    publish_date = datetime.datetime.now().strftime('%Y-%m-%d')
    emp = Mrticle.objects.get(pk=int(id))
    emp.title = title
    emp.status = status
    emp.content = content
    emp.create_date=create_date
    emp.publish_date=publish_date
    print(emp,type(emp))
    emp.save()
    if title:
        return JsonResponse({"error":"0"})
    else:
        return JsonResponse({"error":1,"msg":"更新失败！"})
def deless(request):
    id = request.GET.get('id')
    print(id)
    Id = Mrticle.objects.filter(id=id)
    if Id:
        Id.delete()
        return JsonResponse({"error": "0"})
    else:
        return JsonResponse({"error": 1, "msg": "删除失败！"})