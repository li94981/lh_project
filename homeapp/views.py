# 导入正则
import re
# 导入json串，httpresponse
from django.http import HttpResponse, JsonResponse
# 用于渲染模板
from django.shortcuts import render
# 跳过csrf
from django.views.decorators.csrf import csrf_exempt
# 导入redis
from redis import Redis
#导入settings，用于APIKEY
from lh_project import settings
# 导入云片类。用于发送验证码
from yanzhengma.send_mess import YunPian
# 导入Code类，生成随机六位
from random_code.rd_code import Code
# 创建redis对象
red = Redis(host='127.0.0.1', port=6379)
# 主页函数
def home(request):
    return render(request,'home.html')
# 登录主页
def login_form(request):
    return render(request, "login_home.html")
# 获取验证码
@csrf_exempt
def user_login(request):
    """
    登录逻辑
    :param request:
    :return:
    """
    # 获取前端三个框的输入值
    mobile = request.POST.get("mobile")
    name = request.POST.get("name")
    code = request.POST.get("code")
    if mobile:
        if name:
            if code:
                res=red.get(mobile+"_2")
                # 获取设置的键
                if res:
                    if res == bytes(code,encoding='utf-8'):
                        return JsonResponse({'state': 1})
                    else:
                        return JsonResponse({'state': 0, 'info': '验证码错误，请重新输入'})
                else:
                    return JsonResponse({'state': 0, 'info': '验证码错误或已失效，请重新获取'})
            return JsonResponse({'state': 0, 'info': '验证码不能为空'})
        return JsonResponse({'state': 0, 'info': '用户名不能为空'})
    return JsonResponse({'state': 0, 'info': '手机号不能为空'})
@csrf_exempt
def get_code(request):
    # 前端获取手机号
    mobile = request.POST.get("mobile")
    if mobile:
        phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7|8]|18\d)\d{8}$')
        res = re.search(phone_pat, mobile)  # 验证手机号是否合法
        if res:#如果手机号合法
            val = red.get(mobile + "_1")  # 判断当前手机号是否已经发送过验证码
            if val:
                return JsonResponse({'state': 1, 'info': '请60秒后，再重新获取'})
            else:
                c = Code()
                code = c.get_code()  # 生成随机验证码
                print(code)
                yun_pian = YunPian(settings.APIKEY)
                yun_pian.send_message(mobile, code)
                red.setex(mobile + "_1", 60, code)
                red.setex(mobile + "_2", 300, code)
                return JsonResponse({'state': 0, 'info': '验证码发送成功'})
        return JsonResponse({'state': 1, 'info': '手机号不合法'})
    return JsonResponse({'state': 1, 'info': '手机号不能为空'})
