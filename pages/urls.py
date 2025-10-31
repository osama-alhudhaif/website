from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # type: ignore
    path('test', views.test, name='test'),
]
