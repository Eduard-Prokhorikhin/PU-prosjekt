# Programvareutvikling-prosjekt

## Innholdsfortegnelse

- [How to set up (and run) Django](#how-to-set-up-and-run-django)
- [The starting files](#the-starting-files)
- [Legge til modeller i DB](#legge-til-nye-modeller-i-databasen)
- [Databasespørringer](#databasespørringer)
- [Oppsett av HTML-sider](#oppsett-av-html-sider)

## How to set up (and run) Django

**Install Django:**

`$ pip install django`

**Check if Django is installed:**

`$ python -m django --version`

**Start up development server:**

`$ python manage.py runserver 8080`

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
       'min_mappe.apps.Min_mappeConfig',
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

## Databasespørringer

`from .models import Post` : importerer modellen (tabellen) for annonser i databasen.

`Post.Objects.all()` : returnerer **alle** instanser av Post i databasen.

`Post.Objects.get(pk=1)` : returnerer en instans av Post i databasen hvor pk (primary key) er 1. Det kan kun være én instans som matcher argumentet.

`Post.Objects.exclude(title='Hammer')` : returnerer alle instanser av Post i databasen utenom de instansene hvor tittelen er _Hammer_.

`Post.Objects.filter(title='Hammer')` : returnerer alle instanser av Post i databasen hvor tittelen er _Hammer_.

`Post.Objects.filter(title__contains='a')` : returnerer alle instanser av Post i databasen hvor tittelen inneholder _a_.

`Post.Objects.filter(title__startswith='s')` : returnerer alle instanser av Post i databasen hvor tittelen starter med _s_.

`Post.Objects.filter(pk__gte=3)` : returnerer alle instanser av Post i databasen hvor pk ≥ 3.

      __lt  : less than (<)
      __lte : less or equal to (≤)
      __gt  : greater than (>)
      __gte : greater or equal to (≥)

Du kan også gi flere argumenter ved å skille de med komma (,):

`Post.Objects.filter(title='Hammer', pk__gte=3)`

Les mer i [dokumentasjonen til Django](https://docs.djangoproject.com/en/4.1/topics/db/queries/).

## Oppsett av HTML-sider

For å sette opp en ny side er det tre (fire) filer du skal redigere.

1.  Opprett en ny HTML-fil under `templates` i rot-mappen. Her kan du legge inn vanlig HTML eller lage dynamisk innhold som tar inn argumenter. Her er de vanligste eksemplene på dynamisk innhold (filnavn: `post_detail.html`):

         {% extends "page.html" %}

         {% block content %}
            <h1>{{ post.title }}</h1>
            <p>Publisert: {{ post.pub_date|date:"d.M Y" }}</p>
            <p>{{ post.text }}</p>
         {% endblock %}

    - I dette tilfellet sier vi med `{% extends "page.html" %}` at denne siden skal lastes inn som en del av `page.html` som i vårt tilfelle inneholder en header og `{% block content %}{% endblock %}` som signaliserer hvor innholdet skal plasseres.
    - `{% block content %}{% endblock %}` er hvor selve innholdet til HTML-siden skal lastes. Her har vi input post som av typen ([modellen](#legge-til-nye-modeller-i-databasen)) Post. Dette gjør at vi kan bruke variabel-parenteser `{{ variabel her }}` til å plassere dynamisk innhold basert på input.
    - Man kan også formatere variablene ved å bruke innebygde format. Les mer [her](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/).

2.  I `min_mappe/views.py` må vi fortelle applikasjonen hvordan den skal åpne en HTML-side. Dette gjør vi ved å definere en funksjon som tar inn parameteret `request` (kan også ta inn flere parametere).

         def post_detail(request, pk):
            post = Post.objects.get(pk=pk)

            components = {
               'post': post,
            }

            return render(request, 'post_detail.html', context=components)

    - Her Har vi det ekstra parameteret `pk` som vi bruker til å finne den tilhørende posten og sender denne til `render()`-funksjonen i `components`-dictionary.
    - Når HTML-filen i punkt 1 refererer til `post` er det denne dictionary den slår opp i for å finne variabelen.

3.  For at HTML-siden skal indekseres (få en egen url-slug) må dette defineres i to like filer kalt `urls.py` i "fant"- og "posts"-mappene.

    - `posts/urls.py`:

            from . import views

            urlpatterns = [
               path('', views.index, name='index'),
               path('<int:pk>/', views.post_detail, name='post_detail'),
            ]

      - Vi importerer `views.py` fra mappen vi befinner oss i for å kunne referere til de viewene vi definerte i punkt 2.

      - Her har vi lagt til to paths. Den første er en indeks-side som laster dersom ingen ytterligere slug er skrevet i url-en (det første parameteret til `path()`). Den andre aksepterer alle heltall (int) som slug og gir dette heltallet variabelnavnet pk.

        - pk i denne pathen er den samme som vi så i punkt 2 som argument i den definerte funksjonen.

      - Det andre parameteret i `path()` peker på hvilket view (se punkt 2) som skal lastes.

      - `name`-parameteret er valgfritt, men gjør det enklere å referere til ulike views url inne i HTML-sider.

    - `fant/urls.py`:

            from . import views

            urlpatterns = [
               path('', views.index, name='index'),
               path('posts/', include('posts.urls'), name='posts'),
               path('post/', include('posts.urls'), name='post_detail'),
               path('admin/', admin.site.urls),
            ]

      - Vi har også her en indeks-path som fanger alle tilfeller hvor det ikke er noen ytterligere slug.

      - Dersom vi har slug "posts/" vil denne peke til filen `urls.py` i "posts"-mappen (altså den som vi nettopp så på). Dersom denne etterfølges av en annen slug, som ikke er spesifisert i `fant/urls.py`, vil resten av slugen behandles av `posts/urls.py`. Det samme gjelder for `post/`.

- Oppsummert med eksempel: url = localhost:8080/post/3/

  1.  Vi blir videresendt fra `fant/urls.py` til `posts/urls.py` som videre behandler det som kommer etter "post/" i url-en.

  2.  `posts/urls.py` henter definisjonen for hvordan man setter opp en side i `posts_detail`-funksjonen som er definert i `posts/views.py`. Her fylles også parameteret `pk` inn som heltallet "3".

  3.  Siden lastes med de tilhørende dataene til databasens post med pk=3, i formatet definert i `post_detail.html`.
