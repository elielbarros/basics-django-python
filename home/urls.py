from django.urls import path
from home import views as home_views


# It is also possible to create a namespace to each url defining app_name.
# So it will be necessary to implement it inside html references like
# blog:example
app_name = 'home'

# Name parameter is configured to be used inside html as an url linking
urlpatterns = [
    path('', home_views.home_view, name='home')
]