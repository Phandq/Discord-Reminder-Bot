# Uses discord.py 1.2.3
#

import discord, random, requests, json, asyncio, configparser
from discord.ext import commands
#from config import token
from datetime import datetime

bot = commands.Bot(command_prefix='!')

# create loop to load cogs by folder path
cogExtensions = ["cogs.ping", "cogs.remind"]

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

@bot.command()
async def sleep(ctx):
    if str(ctx.author) == "Dreadin#9400":
        await ctx.send("Shutting down...\n\U0001f44b")
        await bot.logout()

conf = configparser.RawConfigParser()
conf.read('config.ini')
token = conf.get('Bot', 'token')

bot.run(token.strip())