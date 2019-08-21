import discord, random
from discord.ext import commands

class Magic8ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def magic8ball(self, ctx):
        responses = [
            'It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            'Do not count on it',
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful'
        ]

        await ctx.send(":8ball: " + random.choice(responses))
    
def setup(bot):
    bot.add_cog(Magic8ball(bot))