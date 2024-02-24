from django.urls import path
from . import views
urlpatterns = [
    path('',view=views.user_registation,name='user_registation')
]
