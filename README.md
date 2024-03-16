How to install django?
- Execute the command: pip install django

How to start project?
- Execute the command: ```django-admin startproject <PROJECT NAME HERE>```

Another way to create django project without create extra directory
- Execute the command : ```django-admin startproject project .```

How start server?
- Execute the command: ```python <manage.py path here> runserver```

To know more about django-admin
- Execute the command: ```django-admin --help```

What is manage.py and your purpose?
- The file manage.py was created with project and has just one function
- It is primordial to define project configurations and load it to execute
- Configure django project settings too > project.settings

What is settings.py and your purpose?
- Configure django settings
- Configure apps, middlewares, validators... etc
- Configure database, language code and timezone

What is urls.py and your purpose?
- Configure routes

Django works with mode MODEL VIEW TEMPLATE like MVC
- View in Django works like a Controller

When create a new app?
- It is interesting to think about app as a page.
- Everything that compound a page must be inside the app.
- If something diverges the page idea it is necessary to move it to another app.

How create a new app?
- Run the command:
- ```python manage.py startapp <NEW_APP_NAME_HERE>```

It will be used an API to get fill the pages
- Access the url:
- https://jsonplaceholder.typicode.com/posts

Install WhiteNoise to serve Django application with static files
- doc: https://whitenoise.readthedocs.io/en/latest/
- Installation: pip install whitenoise
- Add WhiteNoise to the MIDDLEWARE list

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
```
- Run collectstatic to collect static files: ```python manage.py collectstatic```
- After that run the server:  ```python <manage.py path here> runserver```