"""sample URL Configuration

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
from django.urls import path,include
from . import views
from django.conf.urls import url

app_name = 'web1'


urlpatterns = [
    
	path('',views.homepage,name='homepage'),
	path("logout/", views.logout_request, name="logout"),
	path("login/", views.login_request, name="login"),
	path("transaction/", views.transaction, name="transaction"),
	url(r'^$', views.button),
	url(r'^output', views.output,name="output"),
]
