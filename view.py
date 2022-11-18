from aiogram import types
from create_bot import bot


async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, привет!' f'Начинаем играть!' 
                           f'Игра про конфеты:по очереди берем не больше максимального количества конфет.'f' Кто взял последним, тот и выиграл')
    
async def choice(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, надо определить уровень игры level: 0 или 1?!')
    
async def choice2(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, надо определить ьаксимальное количество конфет!')
    
async def choice3(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, надо определить количество за один раз!')
    
    
    
    
    
    
