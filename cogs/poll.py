import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def poll(self, ctx):
        poll = await ctx.send("```" + '{}: {}'.format(ctx.author, ctx.message.content) + "```")
        #await poll # repeat user poll
        await poll.add_reaction("\U0001F44D") #👍
        await poll.add_reaction("\U0001F937") #🤷
        await poll.add_reaction("\U0001F44E") #👎

def setup(bot): 
    bot.add_cog(Poll(bot))

# !poll Do you like apples?
# !poll 2 Favorite food? 1.Hamburger 2.Pizza
#  