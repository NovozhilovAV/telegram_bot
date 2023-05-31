from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN
from skripts.get_weather import get_weather_spb
from skripts.get_vacancy_python import get_random_vacancy
from skripts.exchange_rates import course

# токен вашего бота, полученный у @BotFather
API_TOKEN: str = BOT_TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))     # реакция на команду help
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')
    # используется фун-я message.answer - ответить и ее параметры

# Этот хэндлер будет срабатывать на команду "/weather"
@dp.message(Command(commands=['weather']))    # реакция на команду weather - погода
async def get_weather_command(message: Message):
    weather = get_weather_spb()
    date = weather[0]
    night = f'\n{weather[2]["weather_day"]} {weather[2]["temperature"]}, {weather[2]["tooltip"]}\n'
    morning = f'\n{weather[3]["weather_day"]} {weather[3]["temperature"]}, {weather[3]["tooltip"]}\n'
    day = f'\n{weather[4]["weather_day"]} {weather[4]["temperature"]}, {weather[4]["tooltip"]}\n'
    evening = f'\n{weather[5]["weather_day"]} {weather[5]["temperature"]}, {weather[5]["tooltip"]}\n'
    await message.answer(date+night+morning+day+evening)

# Этот хэндлер будет срабатывать на команду "/vacancy"
@dp.message(Command(commands=['vacancy']))    # реакция на команду vacansy - вакансии python
async def get_vacancy_command(message: Message):
    vacancies = get_random_vacancy()
    text = 'Three random vacanci Python'
    first_vc = f"Вакансия {vacancies[1]['name']}\nЗарплата {vacancies[1]['salary']}" \
               f"\nДата публикации {vacancies[1]['created_at']}\nСсылка {vacancies[1]['url']}\n"
    second_vc = f"Вакансия {vacancies[2]['name']}\nЗарплата {vacancies[2]['salary']}" \
                f"\nДата публикации {vacancies[1]['created_at']}\nСсылка {vacancies[2]['url']}\n"
    third_vc = f"Вакансия {vacancies[3]['name']}\nЗарплата {vacancies[3]['salary']}" \
               f"\nДата публикации {vacancies[1]['created_at']}\nСсылка {vacancies[3]['url']}\n"

    await message.answer(first_vc)
    await message.answer(second_vc)
    await message.answer(third_vc)

# Этот хэндлер будет срабатывать на команду "/exchange_rates"
@dp.message(Command(commands=['course']))    # реакция на команду - курс валют
async def get_course_command(message: Message):
    exchange = course()
    row_dict = f"Цифр.код': code[0],Букв.код': code[1],'Валюта': new_row[1],'Кол-во едениц': new_row[2].strip(' ')," \
               f"'Курс': new_row[4]}"
    
    # first_ex = f"Цифр.код{}\nБукв.код{'code_lit'}\nВалюта{'name_rate'}" \
    #            f"\nЕденицы{'counte_rate'}\nКурс{'prise_rate'}"

    # first_ex = f"Цифр.код{exchange[1]['code_num']}\nБукв.код{exchange[1]['code_list']}" \
    #            f"\nВалюта{exchange[1]['name_rate']}\nЕденицы{exchange[1]['counte_rate']}" \
    #            f"\nКурс{exchange[1]['prise_rate']}"

    await message.answer(first_ex)

# Этот хэндлер будет срабатывать на отправку боту фото
@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

# Этот хэндлер будет срабатывать на отправку боту стикера
@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)

# Этот хэндлер будет срабатывать на отправку боту любого сообщения
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)



# Регистрируем хэндлеры
# dp.message.register(process_start_command, Command(commands=["start"]))
# dp.message.register(process_help_command, Command(commands=['help']))
# dp.message.register(send_photo_echo, F.photo)
# dp.message.register(send_sticker_echo, F.sticker)
# dp.message.register(send_echo)


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
# @dp.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text='Данный тип апдейтов не поддерживается '
#                                  'методом send_copy')




if __name__ == '__main__':
    dp.run_polling(bot)
