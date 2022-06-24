import re

from django.shortcuts import render
from django.urls import reverse


class adminMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # 调用 view 之前的代码

        path=request.path
        print("请求路径"+path)
        if re.match("^/login"):
            response = self.get_response(request)
        else:
            if request.session.get("username","") !="":
                response = self.get_response(request)
            else:
                return render(request,"index.html")
        return response