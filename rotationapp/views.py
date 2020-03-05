import json

import time

from django.core.paginator import Paginator

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect

from django.views.decorators.csrf import csrf_exempt

from rotationapp.models import Pic





@csrf_exempt
def index(request):

    name2 = request.session.get('name')
    print(name2,22222)
    if name2==None:
        return redirect("homeapp:login_form")
    else:
        print(name2)
        return render(request, 'home.html',{'name2':name2})
@csrf_exempt
def tuichu(request):
    del request.session['name']
    return redirect("homeapp:login_form")
@csrf_exempt
def get_data(request):
    """
    返回页面所需的用户的json数据
    :param request:
    :return:
    """

    # 获取请求所带参数
    row_num = request.GET.get("rows")
    page_num = request.GET.get("page")
    user_list = Pic.objects.all().order_by("id")
    print(user_list)
    all_page = Paginator(user_list, row_num)
    page_list = Paginator(user_list, row_num).page(page_num)
    data = {
        "page": page_num,
        "total": all_page.num_pages,
        "records": all_page.count,
        "rows": list(page_list)
    }
    def myDefault(u):
        if isinstance(u,Pic):
            return {
                "id": u.pk,
                "title":u.title,
                "status":u.zhuangtai,
                "description":u.miaoshu,
                "createDate":u.datetime.strftime('%Y-%m-%d'),
                "url": u.headpic.url,
            }
    user_json = json.dumps(data, default=myDefault)
    return HttpResponse(user_json)
@csrf_exempt
def edit(request):

    """
    编辑用户的实现
    :param request:
    :return:
    """
    # 获取所需参数
    oper = request.POST.get("oper")
    print(oper)
    name = request.POST.get("title")
    zhuangtai = request.POST.get("status")
    miaoshu = request.POST.get("description")
    # pwd = request.POST.get("")
    if oper == "edit":
        id = request.POST.get("id")
        user = Pic.objects.get(pk=id)
        user.title = name
        user.zhuangtai=zhuangtai
        user.miaoshu = miaoshu
        user.save()
    elif oper == "del":
        id = request.POST.get("id")
        Pic.objects.get(pk=id).delete()
    return HttpResponse()
@csrf_exempt
def add_banner(request):
    timess = time.strftime('%Y-%m-%d')
    name = request.POST.get("name")
    status = request.POST.get("status")

    miaoshu = request.POST.get("miaoshu")
    pic = request.FILES.get("pic")
    print(name, status, type(pic))
    if status != None or name !=None or pic != None or miaoshu != None:
        Pic.objects.create(title=name,zhuangtai=status,headpic=pic,miaoshu=miaoshu,datetime=timess)
        return JsonResponse({"error":"0"})
    else:
        return JsonResponse({"error":1,"msg":"请认真填写信息！"})
@csrf_exempt
def updateemp(request):
    id = request.POST.get("id")
    print(id)
    name = request.POST.get("name")
    print(name)
    status = request.POST.get("status")


    miaoshu = request.POST.get("miaoshu")
    emp = Pic.objects.get(pk=id)
    emp.title = name
    emp.zhuangtai = status
    emp.miaoshu = miaoshu
    print(emp.title,emp.zhuangtai)
    emp.save()
    if status != None or name !=None:
        return JsonResponse({"error":"0"})
    else:
        return JsonResponse({"error":1,"msg":"更新失败！"})
@csrf_exempt
def deless(request):
    id = request.POST.get('id')
    print(id)
    Id = Pic.objects.get(pk=id)
    if Id:
        Id.delete()
        return JsonResponse({"error": "0"})
    else:
        return JsonResponse({"error": 1, "msg": "删除失败！"})