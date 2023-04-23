from discord.ext import commands
from discord.commands import slash_command

from ezcord import emb


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="hello")
    async def hello(self, ctx):
        await emb.success(ctx, f"Hello! {ctx.author.mention}", ephemeral=True)


def setup(bot):
    bot.add_cog(Basic(bot))
