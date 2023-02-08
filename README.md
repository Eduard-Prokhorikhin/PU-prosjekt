# Programvareutvikling-prosjekt

## How to set up Django

**Install Django:**

`$ pip install django`

**Check if Django is installed:**

`$ python3 -m django --version`

**Start up development server:**

`$ python3 manage.py runserver 8080`

You can now find the server at localhost:8080

## The starting files

- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
- The inner `fant/directory` is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
- `fant/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
- `fant/settings.py`: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
- `fant/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
- `fant/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
- `fant/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

## Legge til nye modeller i databasen

1. Endre på `models.py` i den respektive mappen (eks. `min_mappe/models.py`)

   Her kan du legge til en ny model slik:

   ```
   class User(models.Model):
       name = models.CharField(max_length=200)
       email = models.CharField(max_length=200)
       phone = models.CharField(max_length=200)
   ```

2. Endre på `min_mappe/apps.py` ved å legge til:

   ```
   class Min_mappeConfig(AppConfig):
       default_auto_field = "django.db.models.BigAutoField"
       name = "min_mappe"
   ```

3. Endre på `fant/settings.py` under INSTALLED_APPS hvor du legger til `min_mappe.apps.Min_mappeConfig`, slik at du får noe lignende som dette:

   ```
   INSTALLED_APPS = [
       'polls.apps.PollsConfig',
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ```

4. Når du er fornøyd med modellen skriver du følgende kommandoer i terminalen:

   `python manage.py makemigrations min_mappe`

   `python manage.py sqlmigrate min_mappe 0001`

   `python manage.py migrate`

   Du skal nå kunne finne de oppdaterte modellene på `localhost:8080/admin/` etter å ha startet opp serveren igjen.
