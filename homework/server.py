# Вывод данных на сайте

# Добавьте на сайт страницу /names, на которой в табличном виде выведите данные о именах новорожденных, 
# получаемые при помощи функции из предыдущей задачи. Пример простейшего оформления таблицы - на следущейм слайде.

from flask import Flask, request
from popular_name import get_name

app = Flask(__name__)

@app.route('/names')
def index():
    # request.args - словарь, ключ - параметр запроса, значение - значение параметра запроса
    # параметров может не быть, поэтому используем get (безопасное чтение из словаря)
    user_year = request.args.get('year')
    url = 'http://api.data.mos.ru/v1/datasets/2009/rows?api_key=b5feac0e7a7244bfeeb5b75115908a47'
    data = get_name(url) 

    result = '<table><tr><th>Имя</th><th>Количество человек</th><th>Год</th><th>Месяц</th></tr>'
    for element in data:
        name = element['Cells']['Name']
        number = element['Cells']['NumberOfPersons']
        year = str(element['Cells']['Year'])
        month = element['Cells']['Month']
        suitable = True
        if user_year is not None:
            if user_year != year:
                suitable = False
        if suitable:
            result += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(name, number, year, month)
        
    result += '</table>'

    return result

if __name__ == '__main__':
    app.run(port=5010, debug=True)