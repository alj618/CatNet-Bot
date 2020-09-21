import discord # импортируем discord.py | pip install discord.py
from discord.ext import commands # discord.ext - фреймворк для создания команд боту, идёт вместе с discord.py
import asyncio # для работы с await / asyncio
import toml_config # конФИГ


conf = toml_config.load_config()["messages"]["errors"]

SUCCESS_LINE = conf["success_line"]["emoji"] * conf["success_line"]["repeat"] + "\n "
SUCCESS_COLOR = conf["success_line"]["color"]

STANDART_LINE = conf["standard_line"]["emoji"] * conf["standard_line"]["repeat"] + "\n "
STANDART_COLOR = conf["standard_line"]["color"]

ERROR_LINE = conf["error_line"]["emoji"] * conf["error_line"]["repeat"] + "\n "
ERROR_COLOR = conf["error_line"]["color"]

INVISIBLE_SYMBOL = conf["invisible_symbol"]


class CogName(commands.Cog): # создаём класс с когом
	
	def __init__(self, bot): # инициализация кога
		self.bot = bot # создание переменной бота

	# код
	@bot.command()
	async def ip(self, ctx, arg):
		response = requests.get( f'https://ipwhois.app/json/{ arg }' )
	 
		user_ip = response.json()['ip']
		user_continent = response.json()['continent']
		user_city = response.json()['city']
		user_code = response.json()['country_code']
		user_flag = response.json()['country_flag']
		user_stol = response.json()['country_capital']
		user_codep = response.json()['country_phone']
		user_region = response.json()['region']
		user_country = response.json()['country']
		user_time = response.json()['timezone_gmt']
		user_val = response.json()['currency']
		user_val_s = response.json()['currency_code']
		user_org = response.json()['org']
		user_timezone = response.json()['timezone']
	 
		global all_info
		all_info = f'\nIP : { user_ip }\nГород : { user_city }\nРегион : { user_region }\nСтолица страны : { user_stol }\nКод телефона : { user_codep }\nКод страны : { user_code }\nСтрана : { user_country }\nВалюта : { user_val }\nВалюта (короткая) : { user_val_s }\nПровайдер : { user_org }\nЗона : { user_timezone }'
	 
		global flag
		flag = f'{ user_flag }'

		emb = discord.Embed(title = 'Пробивка по айпи для мамкиного хацкера', description = f'{ all_info }',colour = SUCCESS_COLOR)
		emb.set_footer(text = f'{bot.user.name} © 2020 | Все права защищены', icon_url = bot.user.avatar_url)
		await ctx.send(embed=emb)

def setup(bot): # функция
	bot.add_cog(CogName(bot)) # добавляем ког 
	print(f"Ког {CogName} готов!") # запуск кога
