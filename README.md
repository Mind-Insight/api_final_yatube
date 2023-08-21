# api_final

Данный api предоставляет возможность пользователям управления такими задачами, как: создание постов, комментариев, их редактирование, удаление и возможность подписываться на пользователей. api имеет простой и интуитивно понятный интерфейс, который вы сможете легко интегрировать в вашу систему. К тому же, данное api обеспечивает безопасность данных с помощью проверки подлинности и авторизации. Можете быть уверены, что ваши данные будут защищены.


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Mind-Insight/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов к API:


Получение списка всех постов:
```http
GET /api/v1/posts
```

Создание нового поста:
```http
POST /api/v1/posts
Authorization: Bearer {token}

{
  "title": "post",
  "content": "string"
}
```

Удаление поста:
```http
DELETE /api/v1/posts/{post_id}
Authorization: Bearer {token}
```

Создание комментария к посту:
```http
POST /api/v1/posts/{post_id}/comments
Authorization: Bearer {token}

{
  "text": "comment"
}
```

Получение информации о конкретном комментарии:
```http
GET /api/v1/posts/{post_id}/comments/{comment_id}
```

Получение списка всех групп:
```http
GET /api/v1/groups
```

Создание подписки на пользователя:
```http
POST /api/v1/follow
Authorization: Bearer {token}

{
  "following": "string"
}
```

## Как внести свой вклад

1. Форкните репозиторий

2. Создайте свою ветку:

```bash
git checkout -b my-feature-branch
```

3. Внесите изменения и зафиксируйте их:

```bash
git commit -am 'Add some feature'
```

4. Загрузите изменения в свой форк:

```bash
git push origin my-feature-branch
```

5. Создайте pull request в оригинальный репозиторий

6. Ожидайте рассмотрения и подтверждения pull request