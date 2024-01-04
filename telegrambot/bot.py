from aiogram import Bot, executor, Dispatcher, types
import asyncio
import logging

from bazakod import find

API_TOKEN = '6920064860:AAFJlI6X52yEPsQn8wuVUMuMTbDDTNmS4kQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Ассалямуалейкум дорогой пользователь!\nЗадай свой вопрос здесь")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    formatted_text = "[Ссылка](https://t.me/M0I_Gospodin)"
    await message.answer(formatted_text, parse_mode="Markdown")


@dp.message_handler()
async def otvet(message: types.Message):
    sms = message.text
    otv = find(sms)
    text = ""
    for i in otv:
        text += i + "—" + otv[i]

    await bot.send_message(message.chat.id, text, parse_mode="Markdown")


# formatted_text = "[Подчеркнутый](https://example.com)"
#     await message.answer(formatted_text, parse_mode="Markdown")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
