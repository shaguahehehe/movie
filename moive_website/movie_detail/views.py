import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from  .models import *
from django.http import HttpResponse,Http404,JsonResponse
# Create your views here.
from  django.views.decorators.cache import  cache_page
def index(request):
    return render(request,"index.html")
# 查询电影
@cache_page(30)
def select_moive(request):
    print("2222")
    if request.method=="GET":
        movies_detail=MovieMessage.objects.all()
        movie_list=str_dict(movies_detail)
        print("测试")
        return JsonResponse(movie_list,safe=False)
# //把所有数据存储在列表
def str_dict(args):
    movie_list=[]
    for i in args:
        context = {}
        context["id"]=i.id
        context["title"] = i.title
        context["info"] = i.info
        context["img"] = i.img
        context["area"] = i.area
        context["type"]=i.type
        context["star"] = i.star
        context["alias"] = i.alias
        context["director"] = i.director
        context["score"] = i.score
        context["language"] = i.language
        context["year"] = i.year
        context["moive_id"] = i.moive_id
        movie_list.append(context)
    return  movie_list

def select_page(request,currpage=1):
    if request.method=="GET":
        movies_detail=MovieMessage.objects.all()
        paginator = Paginator(movies_detail, 8)
        if currpage <= 1:
            currpage = 1
        elif currpage >= paginator.num_pages:
            currpage = paginator.num_pages
        movies_detail = paginator.page(currpage)
        movie_list=str_dict(movies_detail)
        return JsonResponse(movie_list,safe=False)


def select_contain(request,currpage=1):
    if request.method=="GET":
        title=request.GET.get("title", "")
        info = request.GET.get("info", "")
        area = request.GET.get("area", "")
        type = request.GET.get("type", "")
        star = request.GET.get("star", "")
        alias=request.GET.get("alias", "")
        director = request.GET.get("director", "")
        language = request.GET.get("language", "")
        contains_data = MovieMessage.objects.filter(type__contains=type, title__contains=title, info__contains=info,
                                                    area__contains=area,star__contains=star, alias__contains=alias,
                                                    director__contains=director,language__contains=language)
        paginator = Paginator(contains_data, 8)
        if currpage <= 1:
            currpage = 1
        elif currpage >= paginator.num_pages:
            currpage = paginator.num_pages
        movies_detail = paginator.page(currpage)
        movie_list = str_dict(movies_detail)
        return JsonResponse(movie_list, safe=False)