from django.shortcuts import render
# from django.http import *

# Create your views here.

from django.http import HttpRequest, HttpResponse
from datetime import datetime
def grettings(request,name_user="JOSUE"):
    html_to_return=f"<h1 style=\"margin:100px 0px 80px 120px ; color:purple \" ><b >Hey {name_user} what's up, dude?</b></h1>"
    return HttpResponse(html_to_return,content_type="text/html",charset="utf-8")
def home(request):
    htmlDoc="<h1 style=\"color:red ;font-size:50px\">Welcome to the Little Lemon restaurant!<h1>"
    
    return HttpResponse(htmlDoc)
def say_hello(request):
    return HttpResponse("Hello World")


def show_date(request):
    date_joined=datetime.now().hour
    return HttpResponse(date_joined)

def welcome_again(request):
    htmlDoc="<h1 style=\"color:yellow ;font-size:80px\">Welcome to the Little Lemon restaurant AGAIN!<h1>"
    return HttpResponse(htmlDoc)


def show_path(request):

    response=HttpResponse("This works yeah!")
    # return HttpResponse(path,content_type="text/html",charset="utf-8")
    
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # These are some attributes of HTTP request object
    # These provides information about the headers of the request object passed
    path=request.path
    scheme=request.scheme
    method=request.method
    addres=request.META["REMOTE_ADDR"]
    user_agent=request.META["HTTP_USER_AGENT"]
    path_info=request.path_info
    host=request.META["HTTP_HOST"]
    # We can modify (add) the headers for
    #the http response object like this

    response=HttpResponse()
    response.headers["user"]="Josue"
    msg=f""" 
        <br>Path: {path}
        <br>Addres: {addres}
        <br>Scheme: {scheme}
        <br>method: {method}
        <br>User Agent: {user_agent}
        <br>Path info: {path_info}
        <br>HOST: {host}

        <br>headers response: {response.headers}
        <br>FULL PATH:{scheme}/{host}{path}

    """
    
    
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    
    return HttpResponse(msg,content_type="text/html", charset="utf-8")
    # return HttpResponse(f"<b style=\"color:brown ;margin-left:20% ;font-size:400%\">Hello your path is: {path} </b>")

def passing_parameters(request,parameter2=500):
    # return HttpResponse(f"Hello your new message is: {message}, and this is the number: {parameter2} message have you received today",content_type="text/html",charset="utf-8")
    
    return HttpResponse(f"Hello your new message is: , and this is the number: {parameter2} message have you received today",content_type="text/html",charset="utf-8")

def dish_to_prepare(request, dish):
    dishes_descriptions={
        "pasta":"Pasta is a type of noodle made of wheat",
        "lasgna":"It's a type of pasta",
        "chessecake":"It's a type of dessert",
        "falafel":"It's a type of soup"
    }
    try:
        # description=dishes_descriptions[dish]
        return HttpResponse(f"Enjoy your dish: {dish} , a little description of this: {dishes_descriptions[dish]}",content_type="text/html",charset="utf-8")
    except :
        return HttpResponse(f"The dish wasn't found I'm sorry",content_type="text/html",charset="utf-8")

def display_email(request):
    return HttpResponse("Everything is ok",content_type="text/html",charset="utf-8")

def handler404(request,exception):
    return HttpResponse("404-Not Found page")