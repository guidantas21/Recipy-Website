1. ## Create remote PostgreSQL database

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