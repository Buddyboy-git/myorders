"""myorders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.urls import path #Original.
#from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from main import views
 
urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('clearfile', views.clearfile),
    path('readfile', views.readfile),
    path('writefile', views.writefile),
    path('helloworld', views.helloworld),
    path('order_input', views.order_input),
    path('ajax_view', views.ajax_view),
    path('ajax_getstore', views.ajax_getstore),
    path('ajax_getproduct', views.ajax_getproduct),
    ] 
