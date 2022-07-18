# Set Up

1. ## Libraries

    1. Django
        - Framework for backend web development in Python:
        ```
        pip install django
        ```

    2. Bootstrap 5
        - Prebuilt forms that can be rendered on the screen:
        ```
        pip install crispy-bootstrap5
        ```

    3. Logging
        - Module that helps to track the execution of the application:
        ```
        pip install logging
        ```



2. ## Create a Django project

    - By running the command bellow, Django will automatically create the default folders and files for the project:
    ```
    django-admin startproject recipy_website
    ```



3. ## Create remote PostgreSQL database

    1. Access [Heroku](https://dashboard.heroku.com/login) to create an app for the website;

    2. Get the Heroku Postgres add-on for free and add it in the website app;

    3. Register the database in the Django project
        - recipy_website/settings.py

            ```
            DATABASES = {
                'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'd5rpasmfsbmpst',
                'USER': 'etkqbbujxbxaca',
                'PASSWORD': 'fcc7529a90ef0acecd72e4db1b7246da32b814585622a25c200a67f8f1729aa0',
                'HOST': 'ec2-3-223-169-166.compute-1.amazonaws.com',
                'PORT': '5432'
                }
            }
            ```

    4. Migrate the new database;
        - run the following command:
            ```
            python manage.py migrate
            ```
        
        - if that doesn't work, it's necessary to install an additional library before running the migrate command:
            ```
            pip install psycopg2-binary
            ```



4. ## Create the main app

    - By running the command bellow, Django will automatically create the default folders and files for the app:
    ```
    python manage.py startapp main
    ```

    - Now, it's necessary to indicate to Django that the main app exists, to do that we have to declare it in settings.py:
        ```
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        
            # declaring the main app
            'main.apps.MainConfig',
        ]
        ```



5. ## Setting up the main app

    - There are some folders and files that need to be added to the main app:
        - urls.py
            - Stores all urls of the app.

        - forms.py
            - Store the classes responsible to build forms (login, sign up, create post).

        - templates
            - Contain all the html templates of the app.

        - templates/main
            - Contains the html related to the main app.

            - base.html
                - It's the template html, all the other html files extends this one

            - home.html
                - Main page for logged users

            - create_post.html

        - template/registration
            - Contains the html related to registration

            - login.html

            - sign_up.html



6. ## Setting up HTML files and Bootstrap5
    1. settings.py;
        ```
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            # declaring the main app
            'main.apps.MainConfig',

            # bootstrap style
            'crispy_forms',
            'crispy_bootstrap5'
        ]


        CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

        CRISPY_TEMPLATE_PACK = "bootstrap5"
        ```

    1. base.html;
        - Add the meta tags 

    2. Go to the [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/) website and copy the link of the CSS and JavScript;

    3. base.html;
        - Place the CSS link in the head and the JavaScript link in the end of the body.

    4. base.html;
        - We are going to use [Jinja](https://jinja.palletsprojects.com/en/3.1.x/), it is basically a way to write something really similar to Python code in a html file.

        - It's necessary to create some "Jinja blocks", that transforms the base.html in a template, the other html files are going to extend it.

        ```
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">

            <!--Bootstrap CSS-->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

            <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
            {% block intro %}{% endblock %}

            {% block content %}
            {% endblock %}
            <!--Bootstrap JavaScript-->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
        </body>
        </html>
        ```

    5. home.html
        - To extend the base.html template, write this line in the top of the file:
            ```
            {% extends 'main/base.html' %}
            ```

        - Then add the Jinja blocks:
            ``` 
            {% block title %}Home{% endblock %}

            {% block intro%}Home{% endblock %}

            {% block content %}

            {% endblock %}
            ```

        - Do the same thing to the other html.files

            
7. ## Setting up the urls and views
    1. Create views related to each html file, example bellow:
        - main/views.py
            ```
            def home(request):
                return render(request, 'main/home.html')
            ```

    2. Now, it's necessary to connect the views with a url:
        - main/urls.py
            ```
            from django.urls import path
            from . import views

            urlpatterns = [
            path('', views.home, name='home'),
            path('home', views.home, name='home'),
            path('create-post', views.create_post, name='create-post'),
            path('sign-up', views.sign_up, name='sign-up'),
            path('login', views.login, name='login'),
            ]
            ```
    
    3. To finish, we need to indicate all the urls of the main app to Django:
        - recipy_website/urls.py
            ```
            from django.contrib import admin
            from django.urls import path, include

            urlpatterns = [
                path('admin/', admin.site.urls),
                # all the urls from the main app
                path('', include('main.urls')), 
            ]
            ```
