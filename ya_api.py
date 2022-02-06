import requests

ya_token = ' '  # ваш токен для доступа к яндекс диску


def get_headers_ya():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {ya_token}'
    }


def create_folder(f_name):
    uri = 'https://cloud-api.yandex.net/v1/disk/resources'
    create = requests.put(f'{uri}?path={f_name}', headers=get_headers_ya())
    return create.status_code


def get_folder(f_name):
    uri = 'https://cloud-api.yandex.net/v1/disk/resources'
    get = requests.get(f'{uri}?path={f_name}', headers=get_headers_ya())
    return get.status_code


def delete_folder(f_name):
    uri = 'https://cloud-api.yandex.net/v1/disk/resources'
    delete = requests.delete(f'{uri}?path={f_name}', headers=get_headers_ya())
    return delete.status_code
