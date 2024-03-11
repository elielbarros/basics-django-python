from django.urls import path
from blog import views

# Here inside blog url it is not necessary to write blog/ because it was
# already defined using the method inside() in project/urls.py

urlpatterns = [
    path('', views.blog),
    path('example/', views.example)
]
