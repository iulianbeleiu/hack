# Django fundamentals

#### Create and activate virtual environment
```
Create virtual environment
    python3 -m venv env

Activate virtual env:
     . env/bin/activate
     \
```

#### Install Django
```
- activate virtual env
- run: pip install django
```

#### Create Django project
```
django-admin startproject tictactoe

Run server:
    cd tictactoe
    python manage.py runserver
```

#### Set up DB, running initial migrations
```
In settings.py:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': '/etc/mysql/my.cnf',
            },
        }
    }

In my.cnf:
    database = db_name
    user = db_user
    password = db_pass
    default-character-set = utf8

- pip install mysqlclient
- show migrations:  python manage.py showmigrations
- run migrations: python manage.py migrate
```

#### Creating an App
```
- python manage.py startapp gameplay
- add app to settings installed apps
- create model classes
- create migrations: python manage.py makemigrations
- it creates: gameplay/migrations/0001_initial.py containing sql executed to database
- see sql that migration will run: python manage.py sqlmigrate gameplay 0001
- run migration: python manage.py migrate
```

#### Admin site
```
- create super user: python manage.py createsuperuser
```