from django.shortcuts import render
from django.http import *
from django.views import View

class Response(View):
    def __init__(self) -> None:
        pass

class ResponseSon(Response):
    def __init__(self) -> None:
        super().__init__()
def home(request):
    htmlDoc="<h1 style=\"color:red ;font-size:50px\">Welcome to the Little Lemon restaurant!<h1>"
    return HttpResponse(htmlDoc,content_type="text/html",charset="utf-8")
def handler400(request,exception):
    return HttpResponseBadRequest("<h1 style=\"margin-top:200px; border-style:dotted;border-color:brown\"> 400 Bad Request! check your link<h1><br><form action=\"#\" ><label for=\"back\"><input type=\"button\" id=\"back\" value=\"Go home \">",content_type="text/html",charset="utf-8")
def handler403(request,exception):
    return HttpResponseForbidden("<h1 style=\"margin-top:200px; border-style:dotted;border-color:brown\"> 403 Dile can't be shared! check your link<h1><br><form action=\"#\" ><label for=\"back\"><input type=\"button\" id=\"back\" value=\"Go home \">",content_type="text/html",charset="utf-8")
def handler404(request,exception):
    return HttpResponseNotFound("<h1 style=\"margin-top:200px; border-style:dotted;border-color:brown\"> 404 Page Not Found! check your link<h1><br><form action=\"#\" ><label for=\"back\"><input type=\"button\" id=\"back\" value=\"Go home \">",content_type="text/html",charset="utf-8")
def handler500(request):
   return HttpResponseServerError("<h1 style=\"margin-top:200px; border-style:dotted;border-color:brown\"> 500 Server Error! check your link<h1><br><form action=\"#\" ><label for=\"back\"><input type=\"button\" id=\"back\" value=\"Go home \">",content_type="text/html",charset="utf-8")