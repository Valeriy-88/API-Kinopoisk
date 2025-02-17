# API Kinopoisk

Проект представляет собой получение данных с сайта Кинопоиск.
Возможности:
1. Пользователь может получить из базы рандомный фильм.
2. Пользователь может получить всю информацию о фильме по его id.
3. Пользователь может получить все сезоны и эпизоды.
4. Пользователь может получить отзывы пользователей.

## Запуск

В командной строке в папке проекта ввести команду

1. Запуск приложения:
```
    main.py
```
## Использование
### 1. Получить из базы рандомный фильм
```
GET /movie/random
HTTP-Params:
api-key: str
```

#### В ответ должен вернуться рандомный фильм из базы кинопоиска.
```
{
“status code”: 200,
“response”: json
}
```

### 2. Получить всю информацию о фильме по его id.
```
GET /movie/{id}
HTTP-Params:
api-key: str

```
#### В ответ должен вернуться фильм из базы кинопоиска.
```
{
“status code”: 200,
“response”: json
}
```

### 3. Получить все сезоны и эпизоды.
```
GET /season
HTTP-Params:
api-key: str
```
#### В ответ должен вернуться все сезоны и эпизоды.
```
{
“status code”: 200,
“response”: json
}
```

### 4. Получить отзывы пользователей.
```
GET /review
HTTP-Params:
api-key: str
```
#### В ответ должны вернуться отзывы пользователей.
```
{
“status code”: 200,
“response”: json
}
```
