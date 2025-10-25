from django.urls import path
from . import views

urlpatterns = [
    # هذا يربط الرابط الرئيسي (http://127.0.0.1:9000/) بدالة index
    path('', views.index, name='index'), 
]