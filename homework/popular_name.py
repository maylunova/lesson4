'''
Получение данных

На сайте портала открытых данных Москвы 
есть таблица с популярными именами новорожденных. 
Напишите функцию, которая получает данные при помощи requests и читает 
содержимое в формате json. 
Для получения данных используйте ссылку:
http://api.data.mos.ru/v1/datasets/2009/rows
'''

import requests
from config import *

def get_name(url):
    names_data = requests.get(url)
    if names_data.status_code == 200:
        return names_data.json()
    else:
        print('Что-то пошло не так')
    

if __name__ == '__main__':
    url = '{}?api_key={}'.format(URL, KEY)
    names_data = get_name(url)
    print(names_data)
