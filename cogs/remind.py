import discord
from discord.ext import commands
from datetime import datetime

class Remind(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def remind(self, ctx):
        currentTime = datetime.strftime(datetime.now(), '%H:%M:%S')
        args = ctx.message.content
        args = args.split(' ')
        #await ctx.send(args)
        unitOfTime = {'h':"hours", 'm':"minutes", 's':"seconds"}
        
        for unit in unitOfTime:
            #await ctx.send(args[1])
            if unit in args[1]: 
                ## TODO: Add condition to check time
                time = int(args[1].replace(unit,''))
                await ctx.send("I will remind you in " + str(time) + " " + unitOfTime[unit] + " to " + args[1])
                await ctx.author.send('test') 
            # else:
            #     await ctx.send("Usage: !remind 2h for hours, 2m for minutes, and 2s for seconds")
        # try:
        #     if "s" in args[2]:
        #         time = int(args[2].replace('s',''))
        #         await ctx.send(args[2])
        #         await ctx.send(ctx.message.author, ("I will remind you in " + time + "seconds to " + args[1]))
        #         # Send reminder in DM
        # except Exception:
        #     pass

def setup(bot): 
    bot.add_cog(Remind(bot))