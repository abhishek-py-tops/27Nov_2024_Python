
from django.urls import path
from myapp.views import *
urlpatterns = [
    
    path("",index,name="index"),
    path("result/<id>",result,name="result"),
    path("sendmail/<id>",sendmail,name="sendmail")
]
