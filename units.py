import requests
from pprint import pprint
from settings import url_root, headers
from message import scroll_command, array_endpoint, params


class APIDecorator:
    def __init__(self, url: str, params: dict, headers: dict):
        self.url = url
        self.params = params
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
    def __init__(self, path_deco: type, request_handler: type):
        self.path_deco = path_deco
        self.request_handler = request_handler

    def make_request(self, endpoint: str, headers: dict = None, endpoint_params: dict = None, params: dict = None):
        if endpoint_params:
            params.update(endpoint_params)

        base_url = f"{self.path_deco.url}{endpoint}"

        request_class = self.request_handler(base_url, params or {}, headers or {})
        return request_class()


def main():
    deco = APIDecorator(url_root, {}, headers)
    request_factory = APIRequestFactory(deco, APIRequest)
    while True:
        print('Выберите команду из списка:\n', scroll_command)
        try:
            user_input = int(input('Введите цифру: '))
        except(ValueError, TypeError):
            user_input = 1
            print('Введено неверное значение. Будет установлено значение по умолчанию')
        endpoint = array_endpoint[user_input]
        if user_input == 1:
            query_params = {}
        elif user_input == 2:
            try:
                print('Введите ID фильма')
                print('Значение поля id должно быть в диапазоне от 250 до 7000000')
                movie_id = int(input('ID фильма: '))
            except(ValueError, TypeError):
                movie_id = 300
                print('Введено неверное значение. Будет установлено значение по умолчанию')
            query_params = {}
            endpoint = endpoint.format(id=movie_id)
        else:
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
                except(ValueError, TypeError):
                    print('Введено неверное значение. Будет установлено значение по умолчанию')
            if movie_id:
                try:
                    if 250 < int(count_elements) < 7000000:
                        query_params['movieId'] = int(movie_id)
                    else:
                        print('Введено неверное значение. Будет установлено значение по умолчанию')
                except (ValueError, TypeError):
                    print('Введено неверное значение. Будет установлено значение по умолчанию')

        status, response = request_factory.make_request(endpoint=endpoint, headers=headers, params=query_params)
        print(f"Status: {status}")
        pprint(response)
        print('')
