from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello, name="shello"),
    path('sform/',views.sform,name='sform'),
    path('sdetails/',views.sall,name="sdetails"),
    path('sdel/<int:id>',views.sdel,name="sdel"),
    path('supdate/<int:id>',views.supdate,name="supdate"),
]