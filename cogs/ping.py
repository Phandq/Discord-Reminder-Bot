import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(":ping_pong: {}ms".format(latency))

def setup(bot): 
    bot.add_cog(Ping(bot))