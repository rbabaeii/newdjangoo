from unicodedata import name
from django.urls import path , include
from django.contrib import admin
from .views import users , logoutt

urlpatterns = [
    path("u/" , users.as_view()),
    path('admin/', admin.site.urls),
    path("logout/" , logoutt.as_view() , name="logout")

]