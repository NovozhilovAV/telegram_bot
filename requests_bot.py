import requests
import time

API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6075701138:AAEsXPPjMlEYYTUKbPhsJRW2MLIwuG1VuJc'

offset: int = -2
timeout: int = 50
updates: dict


def do_something() -> None:
    print('был апдейт')

while True:
    print('wait')
    stat_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

        end_time = time.time()
        print(f'Время между запросами к Telegram Bot API: {end_time - stat_time}')
