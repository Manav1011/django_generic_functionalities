
## How to make a custom user model in Django

This markdown file will walk you through the steps on how to make a custom user model in Django.

### Requirements

* Django 3.2 or higher
* Python 3.7 or higher

### Steps

1. Create a new Django project.
2. Create a new app named `custom_user`.
3. In the `custom_user` app, create a new file named `models.py`.
4. In the `models.py` file, create a new class named `CustomUser` that extends the `AbstractUser` class.
5. In the `CustomUser` class, define the following fields:
   * `email`: A `models.EmailField` with unique=True.
   * `USERNAME_FIELD`: The field that will be used as the username for authentication. Set this to `email`.
   * `REQUIRED_FIELDS`: An iterable of field names that are required when creating a new user. Set this to an empty iterable.
6. In the `custom_user` app, create a new file named `managers.py`.
7. In the `managers.py` file, create a new class named `CustomUserManager` that extends the `BaseUserManager` class.
8. In the `CustomUserManager` class, define the following methods:
   * `create_user()`: This method creates a new `CustomUser` instance.
   * `create_superuser()`: This method creates a new `CustomUser` instance with superuser privileges.
9. In the `custom_user` app, create a new file named `admin.py`.
10. In the `admin.py` file, import the `admin` module and the `UserAdmin` class from Django's `contrib.auth` module.
11. In the `admin.py` file, create a new class named `CustomUserAdmin` that inherits from the `UserAdmin` class.
12. In the `CustomUserAdmin` class, override the following attributes:
    * `add_form`: Set this to the `CustomUserCreationForm` class.
    * `form`: Set this to the `CustomUserChangeForm` class.
    * `model`: Set this to the `CustomUser` class.
    * `list_display`: Set this to a list of field names that you want to display in the Django admin.
    * `list_filter`: Set this to a list of field names that you want to use as filters in the Django admin.
    * `fieldsets`: Set this to a list of fieldsets that you want to use in the Django admin.
    * `search_fields`: Set this to a list of field names that you want to allow users to search by in the Django admin.
    * `ordering`: Set this to a list of field names that you want to use to order the results in the Django admin.
13. In the `custom_user` app, create a new file named `forms.py`.
14. In the `forms.py` file, import the `UserCreationForm` and `UserChangeForm` classes from Django's `contrib.auth` module.
15. In the `forms.py` file, create two new classes named `CustomUserCreationForm` and `CustomUserChangeForm` that inherit from the `UserCreationForm` and `UserChangeForm` classes, respectively.
16. In the `CustomUserCreationForm` class, override the following attribute:
    * `fields`: Set this to a list of field names that you want to allow users to enter when creating a new `CustomUser` instance.
17. In the `CustomUserChangeForm` class, override the following attribute:
    * `fields`: Set this to a list of field names that you want to allow users to change when editing a `CustomUser` instance.

That's it! You have now created a custom user model in Django.

### Additional resources

* [Django documentation on custom user models](https://docs.djangoproject.com/en/stable/topics/auth/customizing/#custom-user-models)
* [Django blog post on custom user models](https://www.djangoproject.com/weblog/2012/oct/22/custom-user-models/)
* [Stack Overflow question on custom user models](https://stackoverflow.com/questions/1964508/django-custom-user-model)
