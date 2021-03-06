"""bracketeer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index),
    path('groups', views.group_list),
    path('group', views.create_group),
    path('group/<int:group_id>', views.group_detail),
    path('bracket/<int:user_id>', views.bracket, name='user-bracket'),
    path('leaderboard', views.leaderboard),
    path('save-bracket', views.save_bracket),
    path('help', TemplateView.as_view(template_name='help.html')),
    path('register', views.Register.as_view(), name='register'),
    path('join/<int:group_id>', views.join_group, name='join-group'),
]
