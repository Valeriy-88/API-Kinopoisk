import requests
from pprint import pprint
from settings import url_root, headers
from message import scroll_command, array_endpoint, params
from random import randint


class APIDecorator:
    def __init__(self, url: str, headers: dict, params: dict = None):
        self.url = url
        self.params = params if params is not None else {}
        self.headers = headers

    def __call__(self, obj):
        return obj(self.url, self.params, self.headers)


class APIRequest:
    def __init__(self, url, params, headers):
        self.url = url
        self.params = params
        self.headers = headers

    def __call__(self, *args):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.status_code, response.json()


class APIRequestFactory:
    def __init__(self, path_deco: APIDecorator, request_handler: APIRequest):
        self.path_deco = path_deco
        self.request_handler = request_handler

    def make_request(self, endpoint: str, headers: dict = None, endpoint_params: dict = None, params: dict = None):
        if endpoint_params:
            params.update(endpoint_params)

        base_url = f"{self.path_deco.url}{endpoint}"

        request_class = self.request_handler(base_url, params or {}, headers or {})
        return request_class()


def get_id_movie(endpoint_movie_id):
    try:
        print('Введите ID фильма')
        print('Значение поля id должно быть в диапазоне от 250 до 7000000')
        movie_id = int(input('ID фильма: '))
    except (ValueError, TypeError, KeyError):
        movie_id = randint(250, 7000000)
        print('Введено неверное значение. Будет установлено значение по умолчанию')

    endpoint = endpoint_movie_id.format(id=movie_id)
    return endpoint


def season_and_review():
    print('По желанию можете ввести доп. параметры. Нажмите Enter чтобы пропустить поле')
    print('Значение поля ID фильма должно быть в диапазоне от 250 до 7000000')
    movie_id = input('Введите ID фильма: ')
    print('Количество отображаемых элементов должно быть в диапазоне от 1 до 250!')
    count_elements = input('Введите количество отображаемых элементов: ')
    query_params = params
    if count_elements:
        try:
            if 0 < int(count_elements) < 250:
                query_params['limit'] = int(count_elements)
            else:
                print('Введено неверное значение. Будет установлено значение по умолчанию')
        except (ValueError, TypeError, KeyError):
            print('Введено неверное значение. Будет установлено значение по умолчанию')
    if movie_id:
        try:
            if 250 < int(movie_id) < 7000000:
                query_params['movieId'] = int(movie_id)
            else:
                print('Введено неверное значение. Будет установлено значение по умолчанию')
        except (ValueError, TypeError, KeyError):
            print('Введено неверное значение. Будет установлено значение по умолчанию')

    return query_params


def main():
    deco = APIDecorator(url_root, headers)
    request_factory = APIRequestFactory(deco, APIRequest)
    while True:
        print('Выберите команду из списка:\n', scroll_command)
        try:
            user_input = int(input('Введите цифру: '))
        except (ValueError, TypeError, KeyError):
            user_input = 1
            print('Введено неверное значение. Будет установлено значение по умолчанию')
        endpoint = array_endpoint[user_input]

        if user_input == 1:
            query_params = {}
        elif user_input == 2:
            get_id_movie(endpoint)
            query_params = {}
        else:
            query_params = season_and_review()

        status, response = request_factory.make_request(endpoint=endpoint, headers=headers, params=query_params)
        print(f"\nStatus: {status}")
        pprint(response)
        print('')
