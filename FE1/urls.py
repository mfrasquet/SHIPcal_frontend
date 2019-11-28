from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('simulator/<str:lang>',views.simulator,name='simulator'),
]