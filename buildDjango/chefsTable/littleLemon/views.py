from django.shortcuts import render

from django.http import HttpResponse

from .models import Menu


# Create your views here.

def hello(request):
    return HttpResponse("Hello World! from little lemon")

def menu_by_id(request, menu_id):
    # menu=Menu.objects.get(pk=menu_id)
    # return HttpResponse("{}: Type of {} cuisine".format(menu.menu_item,menu.cuisine))

    # 
    return HttpResponse("{}: Type of {} cuisine".format(menu_id,menu_id))



