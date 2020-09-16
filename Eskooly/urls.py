"""Eskooly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Eskooly_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.loginview,name='login'),
    path('dashboard/',views.adminview,name='adminview'),
    path('logout/',views.logoutview,name='logout'),
    path('Add_class/',views.Classes_Entry,name='addclass'),
    path('Add_class/',views.Addclass.as_view(),name='addclass'),
    path('All_Class/',views.All_Classes.as_view(),name='allclass'),
    path('Edit_Class/',views.Edit_class.as_view(),name='editclass'),
    path('delete/<pk>',views.DeleteClass.as_view()),
    path('update/<pk>',views.UpdateClass.as_view()),
]
