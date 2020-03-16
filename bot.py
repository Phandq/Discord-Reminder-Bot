# Uses discord.py 1.2.3
#

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

# create loop to load cogs by folder path
cogExtensions = ["cogs.magic8ball", "cogs.ping", "cogs.quotes", "cogs.remind", "cogs.poll"]

for extension in cogExtensions:
    try:
        bot.load_extension(extension)
    except Exception:
        print(f"Failed to load extension: {extension}")

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
# Add vote, using emoji - reaction poll https://github.com/stayingqold/Poll-Bot/tree/master/cogs
# Add polls https://github.com/Kati3e/KatBot-Discord
# Birthday notification?
# Incorporate DB
# Pillow (image manupulation)
# Game notification (ex. TFT news)
# Get weather
# Simple plugin that logs every message to file
# Reminder that is sent through a DM