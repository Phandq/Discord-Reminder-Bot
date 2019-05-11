# Client ID : 574722367478300673
# Token ID : NTc0NzIyMzY3NDc4MzAwNjcz.XM9iMA.GCz6rgsnZtqAtfLe2fgPuPzTEz8
# Permission integer : 67584

import discord

client = discord.Client()

@client.event # event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event 
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

client.run("NTc0NzIyMzY3NDc4MzAwNjcz.XM9iMA.GCz6rgsnZtqAtfLe2fgPuPzTEz8")


