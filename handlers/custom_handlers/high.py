from loader import bot
from telebot.types import Message
from api import api
from states.variables import Variables


@bot.message_handler(commands=['high'])
def high(message: Message) -> None:
    bot.set_state(message.from_user.id, Variables.max_price, message.chat.id)
    bot.send_message(message.chat.id, 'Введите требуемое количество самых дорогих вариантов:')


@bot.message_handler(state=Variables.max_price)
def get_high(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['max_price'] = message.text
    for elem in api.json_dict['data'][(len(api.json_dict['data']) - int(data['max_price'])):len(api.json_dict['data'])]:
        price = elem['price']
        departure_at = elem['departure_at']
        return_at = elem['return_at']
        bot.send_message(message.chat.id, f'Дата и время вылета в Тбилиси: {departure_at}\n'
                                          f'Дата и время возврата в Москву (Внуково): {return_at}\n'
                                          f'Стоимость билетов: {price}\n')
    bot.delete_state(message.from_user.id, message.chat.id)
