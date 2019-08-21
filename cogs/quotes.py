import discord, requests, json, asyncio
from discord.ext import commands
from concurrent.futures import ProcessPoolExecutor

class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def inspirationalQuote(self): # Get quote from api
        response = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json")
        responseJson = json.loads(response.text)
        author = responseJson['quoteAuthor']
        quote = responseJson['quoteText']
        # test output of json in terminal
        print(responseJson)
        if author == "":
            author = "Anonymous"

        return ("```" + quote + " - " + author + "```") 

    @commands.command()
    async def quote(self, ctx):
        # Invoke sync method from async method
        loop = asyncio.get_running_loop()
        quote = await loop.run_in_executor(None, self.inspirationalQuote)
        await ctx.send(quote)

def setup(bot): 
    bot.add_cog(Quotes(bot))