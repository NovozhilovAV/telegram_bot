import requests
from bs4 import BeautifulSoup
# import fake-useragent import UserAgent

def get_weather_spb() -> list:

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    URL: str = 'https://world-weather.ru/pogoda/russia/saint_petersburg/7days/'
    response = requests.get(URL, headers=headers)
    html = response.text

    # print(response.status_code)

    # with open('weather_site.html', 'rb') as file_html:
    #     html = file_html.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    date: str = soup.find('div', class_='dates short-d').text
    # 'Вторник, 18 апреля'
    table_weather_today = soup.find('table', class_='weather-today short')
    # <table class="weather-today short"><tr class="night"><td class="weather-day">Ночь<......

    rows_table_today = table_weather_today.find_all(name='tr')
    weather_day_list: list = [dict]

    for row in rows_table_today:
        info_weather: dict = {str: str}
        info_weather['weather_day'] = row.find('td', class_='weather-day').text
        info_weather['temperature'] = row.find('td', class_='weather-temperature').text
        info_weather['tooltip'] = row.find('div')['title']
        info_weather['weather-feeling'] = row.find('td', class_='weather-feeling').text
        info_weather['weather-humidity'] = row.find('td', class_='weather-humidity').text
        weather_day_list.append(info_weather)

    weather_day_list.insert(0, date)
    return weather_day_list

for i in get_weather_spb():
    print(i)

if __name__ == '__main__':
    print(get_weather_spb())

    # my_weather: list
    # my_weather = get_weather_spb()
    # print(my_weather[2])