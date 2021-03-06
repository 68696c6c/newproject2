"""newproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app.views import HomeView
from app.views import RockDetail
from app.views import RockList
from app.views import CreateRock
from app.views import UpdateRock
from app.views import DeleteRock

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('home/', HomeView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # Rocks
    path('rocks/list', RockList.as_view(), name='rocks'),
    path('rocks/detail/<int:id>', RockDetail.as_view(), name='rock'),
    path('rocks/create', CreateRock.as_view(), name='create_rock'),
    path('rocks/update/<int:pk>', UpdateRock.as_view(), name='update_rock'),
    path('rocks/delete/<int:pk>', DeleteRock.as_view(), name='delete_rock'),
]
