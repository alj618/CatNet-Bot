import discord
from discord.ext import commands
from loguru import logger
import asyncio
import toml_config

config = toml_config.load_config()
bot = commands.Bot(command_prefix=f'{config["bot"]["prefix"]}', case_insensitive=True)


@bot.event
async def on_ready():
    """
    Информация о запуске бота
    """
    logger.info(f"Бот вошёл в сеть. Аккаунт: {bot.user}, ID аккаунта: {bot.user.id}")


if __name__ == "__main__":  # если запускаем именно этот файл то входим в бота
    bot.run(f'{config["discord"]["token"]}')
