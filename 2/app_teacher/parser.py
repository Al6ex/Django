import requests
import json

# params = {
#     'text': 'NAME:Аналитик',  # Текст фильтра. В имени должно быть слово "Аналитик"
#     'area': 1,  # Поиск ощуществляется по вакансиям города Москва
#     'page': 1,  # Индекс страницы поиска на HH
#     'per_page': 100  # Кол-во вакансий на 1 странице
# }

# req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API

vacancy_id = 55508596
url = f'https://api.hh.ru/vacancies/{vacancy_id}'
response = requests.get(url=url)

if response.status_code != 200:
    print("Ошибка: " + str(response.status_code))
else:
    print(response.content)
    data = response.content.decode()

    with open("vacancy.json", "w", encoding='utf8') as file:
        file.write(json.dumps(data, ensure_ascii=False))

    data