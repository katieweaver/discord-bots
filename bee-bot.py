import os
import random

import discord
from dotenv import load_dotenv

from parse_script import bee_movie

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    #This is to keep the bot from reacting to other bots or itself.
    if message.author == client.user:
        return


    if message.content == 'bees!':
        generator = bee_movie()
        for item in generator:
            #print(item)

            await message.channel.send(item)

client.run(TOKEN)