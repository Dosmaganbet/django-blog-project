# Django Blog

Блог на Django: посты (черновик / опубликован), категории, теги и комментарии с модерацией.

## Запуск

```bash
pip install "Django>=6.0,<6.1"
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Посты создаются в админке (`/admin/`); на сайте видны только опубликованные.
Поле `active` у комментария скрывает его на сайте.

## Тесты

```bash
python manage.py test
```

Настройки через переменные окружения: `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`.
