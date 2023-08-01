import telebot
from telebot import types
import requests

TOKEN = 'Ваш токен BotFather'
WEATHER_API_key = 'Ваш токен https://openweathermap.org/api'

city = 'Minsk'
bot = telebot.TeleBot(TOKEN)


#Кнопки:
# 1. Хочу анекдот
# 2. Хочу отдохнуть
# 3. Прогноз погоды
def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()

    joke_button = types.InlineKeyboardButton(text='😂 Хочу анекдот!',callback_data='1')
    sleep_button = types.InlineKeyboardButton(text='😔 Хочу отдохнуть!',callback_data='2')
    weather_button = types.InlineKeyboardButton(text='🌅 Погода!', callback_data='3')

    keyboard.add(joke_button, sleep_button, weather_button)
    return keyboard



@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id,'Привет {0.first_name}! \nВас приветствует mrSmeley_BOT! \nВыберите, что вы хотите: '.format(message.from_user),reply_markup=create_keyboard())

@bot.callback_query_handler(func= lambda call: True if call.message else False)

def callback_inline(call):
        if call.data == '1':
            res = requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=1")
            bot.send_message(call.message.chat.id, res.text, reply_markup=create_keyboard())
        if call.data == '2':
            bot.send_message(call.message.chat.id, 'Приятного отдыха!')
        if call.data == '3':
            bot.send_message(call.message.chat.id, 'Введите название города на английском!\nНапример "Minsk"')
            @bot.message_handler(func=lambda message: True)
            def get_city(message):
                city = message.text
                res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_key}")
                weather_data = res.json()
                bot.send_message(call.message.chat.id,  f"Погода в городе {city}:\n\n"
                                                        f"Температура: {weather_data['main']['temp']}°C\n"
                                                        f"Влажность: {weather_data['main']['humidity']}%\n"
                                                        f"Скорость ветра: {weather_data['wind']['speed']} м/с\n", reply_markup=create_keyboard())

bot.polling(none_stop=True)