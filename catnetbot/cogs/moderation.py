import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="hello",  # основное имя d
        aliases=[],  # вариации ввода команды
        description="Бот приветствует участника, который вызвал команду",  # описание команды
        usage="hello"  # пример использование команды
    )  # декоратор, говорящий боту, что создана команда
    async def command_hello(self, ctx):  # создание функции с командой
        await ctx.send(f"Hello, {ctx.author}")

def setup(bot):
    bot.add_cog(Moderation(bot))

