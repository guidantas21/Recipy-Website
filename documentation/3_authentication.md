# Basic Authentication Set Up

# Login
- Django has its own [authentication system](https://docs.djangoproject.com/en/4.0/topics/auth/), what makes the delelopment of this feature a lot easier. Firstly, it's necessary to include the prebuilt urls the django provides (login, logout, sign-up, password_change, password_change_done, password_reset, password_reset_done, password_reset_confirm, password_reset_complete) in the urlpatterns list (recipy_website/urls.py).

    ```
    urlpatterns = [
    path('admin/', admin.site.urls),
    # all the urls from the main app
    path('', include('main.urls')),
    # prebuilt urls that automatically do things like log in, log out, password reset...
    path('', include('django.contrib.auth.urls')), 
    ]
    ```

- By doing it we should be able to access the login page, but the page is empty, we need to implement the login forms in our login.html file. Luckly, Django also makes it very easy, we don't need to build the login form form scratch, only load the prebuilt crispy login form inside our content block. Also, every time we are creating a post method form, it's necessary to implement the [csrf_token](https://docs.djangoproject.com/en/4.0/ref/csrf/), which is basically a security feature. 

    ```
    {% extends 'main/base.html' %}

    <!--loading the crispy forms-->
    {% load crispy_forms_tags %}

    {% block title %}Login{% endblock %}

    {% block intro%}Login{% endblock %}

    {% block content %}
    <form method="post">
        <!--Security feature used everytime you have form method post-->
        {% csrf_token %} 
        <!--prebuilt login form-->
        {{form|crispy}}
        <p>Don't have an account? Create one <a href="/sign-up">here</a>!</p>
        <button type="submit" class="btn btn-warning" data-toggle="button" aria-pressed="false" autocomplete="off">
            Login
        </button>
    </form>

    {% endblock %}
    ```

- Django already handles the login view, so we don't need to code it.

- To finish the login implementation for now we need to set some definitions in the settings.py, we have to tell Django that after the user is logged in, he needs to be redirected to the home page, and when the user logged out, he needs to be redirected to the login page, so he can login.

    ```
    LOGIN_REDIRECT_URL = '/home'
    LOGOUT_REDIRECT_URL = '/login'
    ```


# Sign Up

- Now we are able to log users, but to do it we need to be able to register users into the database. For the sign up page it's a little bit different, we have to do it by ourselves, but still simple to be done. Firstly we need to create the registration form in the forms.py, to do it we need to create a class that extends the Django [UserCreationForm](https://www.javatpoint.com/django-usercreationform), passing our User model and the field that user need to fill. In this case we are going to require the email, the username, the password (and password confirmation), first name and last name (both of them are optional).

    ```
    from django import forms
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.models import User

    # this class extends the UserCreationForm
    class RegistrationForm(UserCreationForm):
        # rewriting the email form to be required, not optional 
        email = forms.EmailField(required=True)

        class Meta:
            # indicating the user model
            model = User
            # passing the prebuilt fields 
            fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    ```

- The next step is to add the form we've created in the sign_up.html file, just like was done with the login page.

    ```
    {% extends 'main/base.html' %}

    {% load crispy_forms_tags %}

    {% block title %}Sign Up{% endblock %}

    {% block intro%}Sign Up{% endblock %}

    {% block content %}
    <form method="post">
        {% csrf_token %} {{form|crispy}}
        <p>Have an account? Login <a href="/sign-up">here</a>!</p>
        <button type="submit" class="btn btn-warning" data-toggle="button" aria-pressed="false" autocomplete="off">
            Register
        </button>
    </form>


    {% endblock %}
    ```

- After that it's necessary to create the sign-up view, which is going to render the sign_up.html file, and handle the requests. Basically, if some data is posted (the user filled the form and posted it), it's going to be saved in a from, and if the form is valid, the user is created and automatically logged in. 

    ```
    def sign_up(request):
        # check if some form was posted
        if request.method == 'POST':
            # create the form with the posted information
            form = RegistrationForm(request.POST)
            # check if the form was filled in correctly
            if form.is_valid():
                # save the new user into the database
                user = form.save()
                # login the new user account
                login(request, user)

                return redirect('/home')
    ```

- Otherwise, if the request is get, it's because the user is trying to access the sign up page to make a registration, so we send to him a blank form, so he can fill it and post with his data and be registered in the system

    ```
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})
    ```

- Lastly, let's register the add an url to the sign up page.

    ```
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
        path('home', views.home, name='home'),
        path('create-post', views.create_post, name='create-post'),
        path('sign-up', views.sign_up, name='sign-up'),
    ]
    ```


    # Logout

    - The logout functionality is very simple to be implemented, we only need to redirect the logged user to the '/logout' url and Django does all the job, no need to write views and the url is already included in the 'django.contrib.auth.urls'. 