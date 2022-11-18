import asyncio
import random

import view
from create_bot import dp
from aiogram import types

import model
from create_bot import bot



async def start(message: types.Message):
    
    await view.hello(message)
    await asyncio.sleep(3)
    await view.choice(message)
    await view.choice2(message)
    await view.choice3(message)
     
async def level(message:types.Message):
    level=int((message.text).split(" ")[1])
    model.set_level(level)
   
    await bot.send_message(message.from_user.id, f'выбран уровень' f' {level}'f':0-это скучный уровень, 1-веселый уровень')
    
async def set_total_candies(message: types.Message):

    count = int((message.text).split(" ")[1])
    model.set_total_candies(count)
    await bot.send_message(message.from_user.id, f'Максимальное количество конфет 'f' {count}')
    
 
async def max_take(message:types.Message):
    player = message.from_user
    model.set_player(player)
    max_take=int((message.text).split(" ")[1])
    model.set_max_take(max_take)
    await bot.send_message(message.from_user.id, f'Максимально количество конфет,которое можно взять за раз,'f' {max_take}')
    dp.register_message_handler(player_turn)
    first_turn = random.randint(0,1)
    if first_turn:
        await await_player(player)
    else:
        await enemy_turn(player)

async def player_turn(message: types.Message):
    player = message.from_user
    model.set_player(player)
    number = model.get_max_take()
    if (message.text).isdigit():
        if 0 < int(message.text) < number:
            total_count = model.get_total_candies()
            player_take = int(message.text)
            total = total_count - player_take
            await bot.send_message(player.id, f'{player.first_name} взял {player_take} конфет, 'f'и на столе осталось {total}')
            if model.check_win(total):
                await bot.send_message(player.id, f'Победил {player.first_name}')
                return
            model.set_total_candies(total)
            await enemy_turn(player)

        else:
            await bot.send_message(message.from_user.id, 'А не многовато ли взял')
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, ' f'вообще-то мы конфеты считаем в цифрах')

async def enemy_turn(player):
    total_count = model.get_total_candies()
    number= model.get_max_take()
    lev=model.get_level()
    if lev == 1:
        if total_count < number:
            enemy_take = total_count
        else:
            enemy_take = (total_count - 1) % number
        total = total_count - enemy_take
        await bot.send_message(player.id, f'Бот взял {enemy_take} конфет, 'f'и на столе осталось {total}')
        if model.check_win(total):
            await bot.send_message(player.id, f'{player.first_name} ты проиграл,'f'тебя дёрнула железяка')
            return
        model.set_total_candies(total)
        await asyncio.sleep(1)
        await await_player(player)

            
    else:
            # total_count = model.get_total_candies()
            # number = model.get_max_take()
        enemy_take = random.randint(1, number)
        total = total_count - enemy_take
        await bot.send_message(player.id, f'Бот взял {enemy_take} конфет, 'f'и на столе осталось {total}')
        if model.check_win(total):
            await bot.send_message(player.id, f'{player.first_name} ты проиграл,'f'тебя дёрнула железяка')
            return 
        model.set_total_candies(total)
        await asyncio.sleep(1)
        await await_player(player)

    
async def await_player(player):
    max_take = model.get_max_take()
    await bot.send_message(player.id, f'{player.first_name}, бери конфеты, но не больше {max_take}')

