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
    # it is prudent identify id type
    # URL Dispatcher
    # https://docs.djangoproject.com/en/4.2/topics/http/urls/
    # 'post/<int:id>/'
    path('<int:id>/', views.post, name='post'),
    path('example/', views.example, name='example')
]
