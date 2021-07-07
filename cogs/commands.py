import discord

from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def granny(self, ctx: commands.Context):
        await ctx.send('Test')

def setup(bot):
    bot.add_cog(Commands(bot))