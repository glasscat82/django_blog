# Blog engene 0.1v  
mini blog on the engine Django 2.0.7
```
Django==2.0.7
Python==3.8.7
db.sqlite3
```

## 0 - создание среды
```
python3.8 -m venv venv
source venv/bin/activate
deactivate  # выход в среду выше
```

## 1 - утанавливать в активированной среде
```
pip install django==2.0.7
pip freeze   # Команда pip freeze выводит все установленные в интерпретатор сторонние пакеты.
```

## 2 - создаем папку и вней проект делаем
```
mkdir app
cd app
django-admin startproject blogengene  # команда которая создает проект, (blogengene - блоговый движок нозвание проекта)
```

## 3 - создание приложения в проекте
```
python manage.py startapp blog
./manage.py runserver 5000
./manage.py migrate
```

## 4 - создание супер пользователя
```
$ python manage.py createsuperuser. Введите имя пользователя и нажмите Enter.
Username: admin. Теперь введите email:
Email address: admin@example.com. И наконец введите пароль. 
Password: ********** Password (again): ********* Superuser created successfully.
```

## 5 /blog/models.py добавить модель и осуществить миграцию
```
./manage.py makemigrations   # создаем миграцию
./manage.py migrate	         # Осуществляем миграцию
./manage.py shell            # можно войти в Django и покодить
p = Post(title='New post', slug='new-slug', body='new post body')
p.save()
pl = Post.objects.create(title='new post2', slug='new-slug-2', body='new 2 post body')
Post.objects.all()    # выводит всех
post = Post.objects.get(slug='new-slug')
post
post = Post.objects.get(slug__iexact='New-slug')    # регистро-независимые
post = Post.objects.filter(slug__contains='New')   # получить несколько
```