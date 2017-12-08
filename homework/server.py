'''
Вывод данных на сайте

Добавьте на сайт страницу /names, на которой в табличном виде выведите 
данные об именах новорожденных, получаемыех при помощи функции get_names(). 
Пример простейшего оформления таблицы - на следущейм слайде.

Фильтрация данных
Ограничьте выводимые данные одним годом. 
Год должен указываться в URL как параметр, например /names?year=2016.
''' 

from flask import Flask, request
from popular_name import get_name
from config import *

app = Flask(__name__)

@app.route('/names')
def index():
    # request.args - словарь, где ключ - параметр запроса, 
    # значение - значение параметра запроса;
    # параметров может не быть, поэтому используем get (безопасное чтение)
    user_year = request.args.get('year')
    url = '{}?api_key={}'.format(URL, KEY)
    data = get_name(url) 

    popular_names_table = '''
    <table>
        <tr>  
            <th>Имя</th>
            <th>Количество человек</th>
            <th>Год</th>
            <th>Месяц</th>
        </tr>
    '''

    for element in data:
        name = element['Cells']['Name']
        number = element['Cells']['NumberOfPersons']
        year = str(element['Cells']['Year'])
        month = element['Cells']['Month']
        suitable = True
        if user_year:
            if user_year != year:
                suitable = False
        if suitable:
            popular_names_table += '''
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            '''.format(name, number, year, month)
        
    popular_names_table += '</table>'

    return popular_names_table

if __name__ == '__main__':
    app.run(port=5010, debug=True)
