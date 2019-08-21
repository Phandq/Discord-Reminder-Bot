# Client ID : 574722367478300673
# Token ID : NTc0NzIyMzY3NDc4MzAwNjcz.XM9iMA.GCz6rgsnZtqAtfLe2fgPuPzTEz8
# Permission integer : 67584

# Uses discord.py 1.2.3

import discord, random, requests, json, asyncio
from discord.ext import commands
from config import token
from datetime import datetime

def getQuote(): # Get quote from api
    response = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json")
    responseJson = json.loads(response.text)
    author = responseJson['quoteAuthor']
    quote = responseJson['quoteText']
    # test output of json in terminal
    print(responseJson)
    if author == "":
        author = "Anonymous"

    return ("```" + quote + " - " + author + "```")

bot = commands.Bot(command_prefix='!')

bot.load_extension("cogs.magic8ball")
bot.load_extension("cogs.ping")
bot.load_extension("cogs.quotes")

@bot.event # event decorator/wrapper
async def on_ready():
    date = datetime.now()
    print("Discord.py API version: " + discord.__version__)
    print(f"{date}: Logged in as {bot.user} ({bot.user.id})")

async def notify():
    await bot.wait_until_ready()
    sendTime = '08:00' # Set time to 24-hour clock
    channel = bot.get_channel(432714034719227907)
    while not bot.is_closed():
        currentTime = datetime.strftime(datetime.now(), '%H:%M')
        if currentTime == sendTime:
            await channel.send("Good morning, @everyone \n" + getQuote())
            print("message sent")
            time = 90
        else:
            time = 1
        await asyncio.sleep(time)

# @bot.command()
# async def ping(ctx):
#     latency = round(bot.latency * 1000)
#     await ctx.send(":ping_pong: {}ms".format(latency))

# @bot.command()
# async def magic8ball(ctx):
#     responses = [
#         ':8ball: It is certain',
#         ':8ball: It is decidedly so',
#         ':8ball: Without a doubt',
#         ':8ball: Yes definitely',
#         ':8ball: You may rely on it',
#         ':8ball: As I see it, yes',
#         ':8ball: Most likely',
#         ':8ball: Outlook good',
#         ':8ball: Yes',
#         ':8ball: Signs point to yes',
#         ':8ball: Reply hazy try again',
#         ':8ball: Ask again later',
#         ':8ball: Better not tell you now',
#         ':8ball: Cannot predict now',
#         ':8ball: Concentrate and ask again',
#         ':8ball: Do not count on it',
#         ':8ball: My reply is no',
#         ':8ball: My sources say no',
#         ':8ball: Outlook not so good',
#         ':8ball: Very doubtful'
#     ]

#     await ctx.send(random.choice(responses))

# @bot.command()
# async def quote(ctx):
#     await ctx.send(getQuote())

@bot.command()
async def sleep(ctx):
    if str(ctx.author) == "Dreadin#9400":
        await ctx.send("Shutting down...\n\U0001f44b")
        await bot.logout()


bot.loop.create_task(notify())

bot.run(token.strip())

# https://pachevjoseph.com/posts/python-discord-bot/ create an event in server
# https://www.devdungeon.com/content/make-discord-bot-python-part-2

# TO DO: 
# Add ping (latency)
# Add quotes?
# Add polls, using emoji?
# Birthday notification?
# Incorporate DB
# Pillow (image manupulation)
# Game notification (ex. TFT news)
# Get weather