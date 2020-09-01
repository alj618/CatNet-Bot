import discord
from discord.ext import commands

SUCCESS_LINE = "<:normal_line:749986920578416734>" * 14 + "\n⠀"
SUCCESS_COLOR = 0x6EE51F

STANDART_LINE = "<:standart_line:749988256350863461>" * 14 + "\n⠀"
STANDART_COLOR = 0xADADAD

ERROR_LINE = "<:error_line:749986920700051518>" * 14 + "\n⠀"
ERROR_COLOR = 0xFF3D43

INVISIBLE_SYMBOL = "⠀"


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            await ctx.message.delete()
        except:
            pass
        finally:
            pass

        async def own_command_error_message(problem, solution):
            embed = discord.Embed(color=ERROR_COLOR)
            embed.add_field(name="Проблема:", value=f"{problem}")
            embed.add_field(
                name=f"{INVISIBLE_SYMBOL}", value=f"{ERROR_LINE}", inline=False
            )
            embed.add_field(name="Решение:", value=f"{solution}")
            await ctx.send(embed=embed)

        if isinstance(error, commands.CommandNotFound):
            await own_command_error_message(
                "Команда не найдена!",
                "Используйте существующую команду,\nкоторая есть в списке `.help`",
            )
        elif isinstance(error, commands.DisabledCommand):
            await own_command_error_message(
                "Команда отключена!",
                "Используйте другую, активированную\n в данный момент команду",
            )
        elif isinstance(error, commands.CommandOnCooldown):

            def make_readable(seconds):
                hours, seconds = divmod(seconds, 60 ** 2)
                minutes, seconds = divmod(seconds, 60)
                return "{:02}ч : {:02}м : {:02}с".format(
                    round(hours), round(minutes), round(seconds)
                )

            await own_command_error_message(
                "Команда с задержкой!",
                f"Используйте данную команду \nпосле `{make_readable(error.retry_after)}` ⏳",
            )


def setup(bot):
    bot.add_cog(Errors(bot))
