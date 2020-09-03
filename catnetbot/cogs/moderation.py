import discord
from discord.ext import commands
import toml_config

conf = toml_config.load_config()["messages"]["errors"]

SUCCESS_LINE = conf["success_line"]["emoji"] * conf["success_line"]["repeat"] + "\n "
SUCCESS_COLOR = conf["success_line"]["color"]

STANDART_LINE = conf["standard_line"]["emoji"] * conf["standard_line"]["repeat"] + "\n "
STANDART_COLOR = conf["standard_line"]["color"]

ERROR_LINE = conf["error_line"]["emoji"] * conf["error_line"]["repeat"] + "\n "
ERROR_COLOR = conf["error_line"]["color"]

INVISIBLE_SYMBOL = conf["invisible_symbol"]


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
            name = "кик",
            aliases = ["kick", "выгнать", "кикнуть"],
            description = "Выгнать игрока с сервера",
            usage = "кик [участник] (причина)",
    )
    @commands.has_permissions(kick_members = True)
    async def moderation_command_kick(self, ctx, member: discord.Member, reason = "Не указана"):
        emb = discord.Embed(color = SUCCESS_COLOR)
        emb.add_field(name = "Выгнан:", value = f"{member}")
        emb.add_field(name = "Выгнал:", value = f"{ctx.author.mention}")
        emb.add_field(name = f"{INVISIBLE_SYMBOL}", value = f"{SUCCESS_LINE}", inline = False)
        emb.add_field(name = "Причина:", value = f"{reason}")
        await ctx.send(embed = emb)
        await member.kick()

def setup(bot):
    bot.add_cog(Moderation(bot))
