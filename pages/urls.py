from django.urls import path
from . import views

urlpatterns = [ # type: ignore
    path('', views.index, name='index'),
    path('/templates', views.templates, name='templates'),
]
