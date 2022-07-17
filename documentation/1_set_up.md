# Set Up

1. ## Libraries libraries

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