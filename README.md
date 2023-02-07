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
