"""
URL configuration for chefsTable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("",views.home,name="index"),
    path('little_lemon/', include("littleLemon.urls"),name="main_little_lemon_home"),
    path("myapp/",include("myapp.urls"),name="main_myapp_home"),
    # path('suburl/', views.home,name="home2")

]
handler400="chefsTable.views.handler400"
handler403="chefsTable.views.handler403"

handler404="chefsTable.views.handler404"
handler500="chefsTable.views.handler500"

