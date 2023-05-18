from django.urls import path
from .views import home, sayt, permission, inform,register,index,git_copy

urlpatterns = [
    path('home/<int:yosh>',home),
    path('sayt/',sayt),
    path('permission/<int:yosh>/',permission),
    path('inform/<str:familiya>/<str:ism>/',inform),
    path('register/',register),
    path('index/',index),
    path('git_copy/',git_copy)
]