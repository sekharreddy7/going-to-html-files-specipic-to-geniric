from django.contrib import admin
from django.urls import path
app_name='app2'
from app2 import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('hello/',views.hello,name='hello'),
]