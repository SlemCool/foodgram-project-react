<div align="head">
  <img src="head.png"/>
</div>

## :man_technologist: Дипломный проект. 

Сайт, на котором пользователи публикуют рецепты, подписываться на публикации других авторов и добавлять рецепты в избранное.
Возможность формировать список покупок из избранных рецептов.

На проекте отточен навык автоматизации процесса деплоя, на удаленный сервер.
При помощи Git Actions: 

![workflow](https://github.com/SlemCool/foodgram-project-react/actions/workflows/main.yaml/badge.svg)

Сайт доступен по адресу [foodgramm.ddns.net](http://foodgramm.ddns.net/)

Документация к API доступна по адресу [foodgramm.ddns.net/api/docs/](http://foodgramm.ddns.net/api/docs/)

### :hammer_and_wrench: Технологии:

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="Django" alt="Django" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" title="Docker" alt="Docker" width="50" height="50"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original-wordmark.svg" title="Git" alt="Git" width="50" height="50"/>
  <img src="https://github.com/devicons/devicon/blob/master/icons/nginx/nginx-original.svg" title="Git" alt="Git" width="50" height="50"/>
  <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original-wordmark.svg" title="Git" alt="Git" width="50" height="50"/>
</div>

### Развернуть проект на удаленном сервере:

- Клонировать репозиторий:
```
https://github.com/SlemCool/foodgram-project-react.git
```

- Установить на сервере Docker, Docker-Compose:

- Скопировать на сервер файлы docker-compose.yml, nginx.conf из папки infra (команды выполнять находясь в папке infra):
```
scp docker-compose.yml nginx.conf <username>@<IP>:/home/username/   # username - имя пользователя на сервере
                                                                    # IP - публичный IP сервера
```

- Создать и запустить контейнеры Docker, выполнить команду на сервере
```
sudo docker-compose up -d
```

- После успешной сборки выполнить миграции:
```
sudo docker-compose exec backend python manage.py migrate
```

- Создать суперпользователя:
```
sudo docker-compose exec backend python manage.py createsuperuser
```

- Собрать статику:
```
sudo docker-compose exec backend python manage.py collectstatic --noinput
```

- Наполнить базу данных содержимым из файла ingredients.json:
```
sudo docker compose exec backend python manage.py loaddata ./data/ingredients.json
```
### Готово! :fire:

Автор backend'а:

Кагадий Андрей 2023г.
