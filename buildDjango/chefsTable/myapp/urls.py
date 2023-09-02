from django.urls import path,re_path
from . import views
urlpatterns=[
    path("remember_passing_paramteres/<str:name_user>",views.grettings,name="remember_passing_parameteres"),
    path("remember_passing_paramteres/",views.grettings,name="remember_passing_parameteres"),

    path("welcome" ,views.home,name="welcome"),
    path("hello" ,views.say_hello,name="hello"),
    path("date" ,views.show_date,name="date"),
    path("welcomeagain" ,views.welcome_again,name="welcagain"),
    path("showpath",views.show_path,name="showing_path"),
    # path("parameter/<str:message>/<int:parameter2>",views.passing_parameters,name="passing_parameters"),
    path("parameter/<int:parameter2>",views.passing_parameters,name="passing_parameters"),
    path("parameter/",views.passing_parameters,name="passing_parameters"),
    path("dishes/<str:dish>",views.dish_to_prepare,name="menu"),
    # figure out how woud be the regular expression for
    #emil_display/Asd2123sadasda232@gmail.com
    # re_path(r'^email_display/([a-zA-Z]+[0-9]*)+@[a-z]+\.[a-z]{2}[a-z]*$',views.display_email,name="email_display")
    re_path(r'^email_display/[a-zA-Z]+[0-9]*@[a-z]+\.[a-z]{2}[a-z]*$',views.display_email,name="email_display"),
]