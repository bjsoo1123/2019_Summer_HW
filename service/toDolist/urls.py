from django.urls import path
from .views import *

app_name = "toDolist"
urlpatterns = [
    path('show/', show, name="show"),
    path('', home, name="home"),
]