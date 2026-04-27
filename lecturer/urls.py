from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello, name="lhello"),
    path('lform/',views.lform,name='lform'),
    path('ldetails/',views.lall,name='ldetails'),
    path('ldel/<int:id>',views.ldel,name='ldel'),
    path('lupdate/<int:id>',views.lupdate,name='lupdate'),
]