## Проект Foodgram
![workflow](https://github.com/AlieD3d/foodgram-project-react/actions/workflows/main.yml/badge.svg)

Foodgram - продуктовый помощник с базой кулинарных рецептов. Позволяет публиковать рецепты, сохранять избранные, а также формировать список покупок для выбранных рецептов. Можно подписываться на любимых авторов.

Проект доступен по [адресу](http://51.250.19.123)

### Технологии:
- Python 
- Django 
- Django REST framework 
- Nginx
- Docker
- Postgres

### Развернуть проект на удаленном сервере:

- Клонировать репозиторий:
```
https://github.com/AlieD3d/foodgram-project-react.git
```

- Установить на сервере Docker, Docker Compose:

```
sudo apt install curl                                   # установка утилиты для скачивания файлов
curl -fsSL https://get.docker.com -o get-docker.sh      # скачать скрипт для установки
sh get-docker.sh                                        # запуск скрипта
sudo apt-get install docker-compose-plugin              # последняя версия docker compose

```
- Выдать права доступа для docker-compose:
```
sudo chmod +x /usr/local/bin/docker-compose
```

- Скопировать на сервер файлы docker-compose.yml, nginx.conf из папки infra:

```
scp -r infra/*  username@IP:/home/username/   # username - имя пользователя на сервере
                                                                # IP - публичный IP сервера
```

- Для работы с GitHub Actions необходимо в репозитории в разделе Secrets > Actions создать переменные окружения:
```
DEBUG=False
SECRET_KEY=<Your_some_long_string>
ALLOWED_HOSTS='localhost, 127.0.0.1, <Your_host>'
CSRF_TRUSTED_ORIGINS='http://localhost, http://127.0.0.1, http://<Your_host>'
DB_ENGINE='django.db.backends.postgresql'
DB_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD=<Your_password>
DB_HOST='db'
DB_PORT=5432
```

- Создать и запустить контейнеры Docker, выполнить команду на сервере
*(версии команд "docker compose" или "docker-compose" отличаются в зависимости от установленной версии Docker Compose):*
```
sudo docker compose up -d
```

- После успешной сборки выполнить миграции:
```
sudo docker compose exec backend python manage.py migrate
```

- Создать суперпользователя:
```
sudo docker compose exec backend python manage.py createsuperuser
```

- Собрать статику:
```
sudo docker compose exec backend python manage.py collectstatic --noinput
```

- Наполнить базу данных содержимым из файла ingredients.json:
```
sudo docker compose exec backend python manage.py loaddata recipes/data/ingredients.json
```

- Для остановки контейнеров Docker:
```
sudo docker compose down -v      # с их удалением
sudo docker compose stop         # без удаления
```

### После каждого обновления репозитория (push в ветку master) будет происходить:

1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8)
2. Сборка и доставка докер-образов frontend и backend на Docker Hub
3. Разворачивание проекта на удаленном сервере
4. Отправка сообщения в Telegram в случае успеха

### Запуск проекта на локальной машине:

- Клонировать репозиторий:
```
https://github.com/AlieD3d/foodgram-project-react.git
```

- В директории infra файл example.env переименовать в .env и заполнить своими данными:
```
DEBUG=False
SECRET_KEY=<Your_some_long_string>
ALLOWED_HOSTS='localhost, 127.0.0.1, <Your_host>'
CSRF_TRUSTED_ORIGINS='http://localhost, http://127.0.0.1, http://<Your_host>'
DB_ENGINE='django.db.backends.postgresql'
DB_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD=<Your_password>
DB_HOST='db'
DB_PORT=5432
```

- Создать и запустить контейнеры Docker, как указано выше.


- После запуска проект будут доступен по адресу: [http://localhost/](http://localhost/)


- Документация будет доступна по адресу: [http://localhost/api/docs/](http://localhost/api/docs/)


### Автор backend'а:

by AlieD3d (c) 2022
