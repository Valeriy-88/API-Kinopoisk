scroll_command = {
    1: 'рандомный фильм',
    2: 'Всю информацию о фильме',
    3: 'Все сезоны и эпизоды',
    4: 'Отзывы пользователей',
}

array_endpoint = {
    1: "/movie/random",
    2: "/movie/{id}",
    3: "/season",
    4: "/review",
}

params = {
    "page": 1,
    "limit": 10,
    "movieId": 500
}
