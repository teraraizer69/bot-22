from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = Bot(token=  '7133783190:AAGYpfR8J4Jrg6p83sxkMJLgNbcqDW1r7M0')
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
button  = KeyboardButton('Клик')
button1 = KeyboardButton('Клик-клик')
keyboard.add(button,button1)

keyboard_Inline = InlineKeyboardMarkup(row_width= 2)
button_Inline = InlineKeyboardButton('Покажи гугл браузер', url='https://www.google.com/')
button_Inline1 = InlineKeyboardButton('Покажи яндекс браузер', url='https://ya.ru/?utm_referrer=https%3A%2F%2Fwww.google.com%2F')
keyboard_Inline.add(button_Inline, button_Inline1)
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы запустить бота'),

    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый ЭХО бот', reply_markup= keyboard)

@dp.message_handler(lambda message: message.text == 'Клик')
async def button_click(message: types.Message):
    await message.answer('Ты кликнул!!', reply_markup= keyboard_Inline)

@dp.message_handler(lambda message: message.text == 'Клик-клик')
async def button1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://avatars.dzeninfra.ru/get-zen_doc/1533996/pub_5e1b40e3d4f07a00af66be98_5e1b41e898fe7900b031bb4c/scale_1200', caption= 'смотри какой я красивый!!')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)