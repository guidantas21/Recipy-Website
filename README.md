1. # Concept

- Recipy is a website which users can share and discover recipes. The concept is similar to social medias like Twetter or Instagram, people can share something to other people see, but the difference is that Recipy is a generator of random recipes that are in the database, they are not ordered. This way, users are more exposed to diferent recipes, not only the most recent ones. So, it's possible to post your own culinary recipes, edit them or delete, also you will be able to search for specific accounts and see all their recipes or search for specific more food and see many possible ways to cook it. 



2. # Technogy used

    1. ### Backend
        - The backend of this website is writen in Python, making use of the [Django](https://www.djangoproject.com/) Framework;
            - This framework is a powerfull tool that make the creation of authentication functionalities, user management, and many other things a lot easier and organized, especially for more complex projects.

        - All the application data will be stored in a remote [PostgreSQL](https://www.postgresql.org/about/) database.
            - PostgreSQL is a free, open source and reliable tool to store data, also it allows multiple access to the database, which means that users can make posts simultaneously, differently from how Sqlite3 works.
            - The database will be hosted remotly for free by a platform called [Heroku](https://id.heroku.com/login), the free version of their service is kinda limited, but enough for the purposes of this project.


    2. ### Frontend
        - The frontend of this application is quite simple, since this project is more focused on the backend and the Django Framework itself;

        - We are using [Bootstrap5](https://getbootstrap.com/) to make the styling of the HTML, it's a very nice framework to render decent forms and make the styling job easier in small projects like this one;


    3. ### Others
        - [Logging](https://docs.python.org/3/library/logging.html)
            - Python library used to track the execution of the application.



3. ## Applications
    - A project is a collection of configuration and apps. A [Django App](https://docs.djangoproject.com/en/4.0/intro/tutorial01/) is basically a module of your project that has a functionality.

    - This project has a project configuration folder called 'recipy_website':
        - urls.py
            - Store all the urls of the project.

        - settings.py
            - This file is responsable to inform Django about the configurations of the project, such as the database, the installed apps, and others... 

    - Also, there's an app folder called 'main':
        - This app is responsible for most of the website functionalities (CRUD, login, sign up...).



4. ## Authentication
    - Using the [Django User Model](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/) and the [Django Authentication System](https://docs.djangoproject.com/en/4.0/topics/auth/default/) was possible to implement user registration and login.
    - Each User has a required username, a required email, first name, last name and a password.
    - It's possible to register, login and logout users. 