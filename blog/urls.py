from django.urls import path
from blog import views

# It is also possible to create a namespace to each url defining app_name.
# So it will be necessary to implement it inside html references like
# blog:example
app_name = 'blog'

# Here inside blog url it is not necessary to write blog/ because it was
# already defined using the method inside() in project/urls.py
# Name parameter is configured to be used inside html as an url linking
urlpatterns = [
    path('', views.blog, name='home'),
    path('example/', views.example, name='example')
]
