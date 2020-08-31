import discord
from discord.ext import commands

import json

import asyncio


config = json.load(open("config.json"))


bot = commands.Bot(command_prefix=f'{config["prefix"]}')


@bot.event
async def on_ready():
	"""
	Информация о запуске бота
	"""
	print(f"Бот вошёл в сеть. Аккаунт: {bot.user}, ID аккаунта: {bot.user.id}")


bot.run(f'{config["token"]}') # запуск бота, надо вставить токен бота который можно получить зайдя в https://discord.com/developers/applications в приложение вашего бота
