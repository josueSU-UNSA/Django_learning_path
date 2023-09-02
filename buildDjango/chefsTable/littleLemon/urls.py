
from django.urls import path
from . import views



urlpatterns = [
    path('', views.hello,name="home"),
    path("menu/<int:menu_id>",views.menu_by_id,name="menu_by_id"),
    # path('suburl/', views.home,name="home2")

]
