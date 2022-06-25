import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
import  hashlib

from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.http import HttpResponse, Http404, JsonResponse
# Create your views here.
from django.views.decorators.cache import cache_page


def index(request):
    return render(request, "index.html")


# 查询电影
@cache_page(30)
def select_moive(request):
    if request.method == "GET":
        movies_detail = MovieMessage.objects.all()
        movie_list = str_dict(movies_detail)
        print("测试")
        return JsonResponse(movie_list)


# //把所有数据存储在列表
def str_dict(args):
    movie_dict = {}
    dianyi=[]
    lianxj=[]
    zongyi=[]
    dongm=[]
    for i in args:
        context = {}
        context["id"] = i.id
        context["title"] = i.title
        context["img"] = i.img
        context["score"] = i.score
        context["year"] = i.year
        context["moive_id"] = i.moive_id
        if i.moive_id ==1:
            dianyi.append(context)
        if i.moive_id == 2:
            lianxj.append(context)
        if i.moive_id == 3:
            zongyi.append(context)
        if i.moive_id == 4:
            dongm.append(context)
    movie_dict["diany"] =dianyi
    movie_dict["lianxj"] = lianxj
    movie_dict["zongyi"] = zongyi
    movie_dict["dongm"] = dongm
    return movie_dict
def select_page(request, currpage=1):
    if request.method == "GET":
        movies_detail = MovieMessage.objects.all()
        paginator = Paginator(movies_detail, 8)
        if currpage <= 1:
            currpage = 1
        elif currpage >= paginator.num_pages:
            currpage = paginator.num_pages
        movies_detail = paginator.page(currpage)
        movie_list = str_dict(movies_detail)
        return JsonResponse(movie_list, safe=False)


def select_contain(request, currpage=1):
    if request.method == "GET":
        title = request.GET.get("title", "")
        info = request.GET.get("info", "")
        area = request.GET.get("area", "")
        type = request.GET.get("type", "")
        star = request.GET.get("star", "")
        alias = request.GET.get("alias", "")
        director = request.GET.get("director", "")
        language = request.GET.get("language", "")
        contains_data = MovieMessage.objects.filter(type__contains=type, title__contains=title, info__contains=info,
                                                    area__contains=area, star__contains=star, alias__contains=alias,
                                                    director__contains=director, language__contains=language)
        paginator = Paginator(contains_data, 8)
        if currpage <= 1:
            currpage = 1
        elif currpage >= paginator.num_pages:
            currpage = paginator.num_pages
        movies_detail = paginator.page(currpage)
        movie_list = str_dict(movies_detail)
        return JsonResponse(movie_list, safe=False)



    # 画出验证码


# 验证码
def captcha(request):
    # 引入绘画模板
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量,用于画面的背景色,宽,高
    bg_color = (random.randrange(20, 100), random.randrange(20, 100), 255)
    bg_width = 100
    bg_height = 25
    # 创建画面对象
    im = Image.new('RGB', (bg_width, bg_height), bg_color)
    # 创建笔画对象
    draw = ImageDraw.Draw(im)
    # 调用笔画的point()函数绘画噪点
    for i in range(0, 100):
        draw_xy = (random.randrange(0, bg_width), random.randrange(0, bg_height))
        draw_fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(draw_xy, fill=draw_fill)
    # 定义验证码的备选值
    candidate_str = 'ASDFGHJKLQWERTYUIO1234567890ZXCVBNM0987654321poiuytrewqlkjhgfdsamnbvcxz'
    # 随机选取四个字符作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += candidate_str[random.randrange(0, len(candidate_str))]
    # 构造字体对象
    font_obj = ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMLI.TTF", 23)

    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制出随机选取的四个字符
    draw.text((5, 0), rand_str[0], font=font_obj, fill=fontcolor)
    draw.text((25, 0), rand_str[1], font=font_obj, fill=fontcolor)
    draw.text((50, 0), rand_str[2], font=font_obj, fill=fontcolor)
    draw.text((75, 0), rand_str[3], font=font_obj, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session, 用于做进一步验证
    request.session['captcha'] = rand_str
    print(request.session['captcha'])
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中,文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端,MIME类型为图片png
    return HttpResponse(buf.getvalue(), content_type='image/png')


# 登录验证
@csrf_exempt
def login(request):
    logininfo=request.body
    logininfo=json.loads(logininfo)
    username=logininfo['username']
    password = logininfo['password']
    captcha = logininfo['captcha']
    if captcha == request.session['captcha']:
        if (~(username == None)):
            try:
                stu1 = Stupwd.objects
                stu = stu1.get(name=username)
                pwd=hashlib.md5()
                pwd.update(password.encode())
                if username == stu.name and stu.pwd == pwd.hexdigest():
                    request.session['username'] = username
                    result = {
                        "code": '200 ',
                        "msg": "登录成功"
                    }
                    return JsonResponse(result)
                else:
                    result = {
                        "code": '206 ',
                        "msg": "账号或密码错误"
                    }
                    return JsonResponse(result)
            except:
                result = {
                    "code": '206 ',
                    "msg": "账号或密码错误"
                }
                return JsonResponse(result)
    else:
        result = {
            "code": '205 ',
            "msg": '验证码错误'
        }
        return JsonResponse(result)
