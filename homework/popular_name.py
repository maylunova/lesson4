#Получение данных

# На сайте портала открытых данных Москвы есть таблица с популярными именами новорожденных. 
# Напишите функцию, которая получает данные при помощи requests и читает содержимое в формате json. 
# Для получения данных используйте ссылку http://api.data.mos.ru/v1/datasets/2009/rows

import requests

def get_name(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('Что-то пошло не так')
    

if __name__ == '__main__':
    data = get_name('http://api.data.mos.ru/v1/datasets/2009/rows?api_key=b5feac0e7a7244bfeeb5b75115908a47')
    print(data)
