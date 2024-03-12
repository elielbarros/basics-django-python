from django.shortcuts import render


# Create your views here.


def home_view(request):
    # To render the page home.html it is necessary to configure the app home
    # created on file settings.py > in INSTALLED_APPS array > add home that
    # is configured at apps.py of home app, HomeConfig > name
    # To prevent collision between others files named 'home.html' it is
    # important to configure namespace on templates
    # To do this it is necessary to create inside directory template another
    # directory with app name, for example, templates > home > template files
    # This strategy is named namespace, this will avoid collision between
    # equal file names.
    
    context = {
        'text': 'You are in home.',
        'title': 'Home Title - '
    }
    
    return render(
            request,
            'home/index.html',  # 'global/base.html'
            context
    )
