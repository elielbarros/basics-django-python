"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

# About method include
# Use include method to join another endpoints to principal created here.
# For example, it is not necessary to repeat blog: blog/article/image/comment
# Using include, it is necessary just add /article/image/comment inside app
# blog.

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
