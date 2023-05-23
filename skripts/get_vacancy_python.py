import requests
from random import randint, sample

def get_random_vacancy():
    URL: str = 'https://api.hh.ru/vacancies?'

    headers: dict = {
        'User-Agent': 'api-test-agent'
    }

    params: dict = {
        'page': '1',
        'per_page': '100',
        'text': 'python',
        'area': '2'
    }

    ids: list = [str]
    resp = requests.get(URL, headers=headers, params=params)
    data = resp.json()
    count_page = data['pages']
    count_id = data['found']

    # print(resp.status_code)
#
    for i in range(count_page + 1):
        resp = requests.get(f'https://api.hh.ru/vacancies?page={i}&per_page=100&text=python&area=2')
        data = resp.json()
        for item in data['items']:
            ids.append(item['id'])
    print(f'found ids = {count_id}, parsed ids = {len(ids)}')
    print(len(set(ids)))

    #rand_id = ids[randint(0, len(ids) - 1)]
    rand_ids = sample(ids, 3)
    list_of_data_vacancy: list = [dict]
#
    for id in rand_ids:
        url_rand_vacancies = f'https://api.hh.ru/vacancies/{id}'
        resp_vacancies = requests.get(url=url_rand_vacancies, headers=headers).json()
        data_vacancy = {'name': resp_vacancies["name"],
                        'created_at': resp_vacancies["created_at"],
                        'salary': resp_vacancies["salary"],
                        'url': resp_vacancies["alternate_url"]
                        }
        list_of_data_vacancy.append(data_vacancy.copy())


    return list_of_data_vacancy

if __name__ == '__main__':
    list_of_vacancy: list = get_random_vacancy()
    for vac in list_of_vacancy:
        print(vac)