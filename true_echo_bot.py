import secret
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = secret.TrainingAleksBotToken

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Карма-бот!\nНапиши мне что-нибудь и получи мгновенное воздояние!')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    # Запоминаем тех, кто просит о помощи
    with open('help.log', 'a') as h:
        print(message.json(exclude_none=True), file=h)
    await message.answer('Скажи мне, кто твой друг '
                         'и я скажу тебе кто ты...')


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        # Логгируем все сообщения
        with open('cash.log', 'a') as cash:
            print(message.json(exclude_none=True), file=cash)
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                 'методом send_copy')


if __name__ == '__main__':
    dp.run_polling(bot)
