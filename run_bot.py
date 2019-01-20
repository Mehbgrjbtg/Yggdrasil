import asyncio
import os
import time
import sys
import aiohttp
import random
import logging
import logging.handlers
import shutil
import traceback

try:
    from discord.ext import commands
    import discord
except ImportError:
    sys.exit()

description = "The beginings of the Yggdrasil-Bot. Made and maintained by Circuitree."

bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), description = description)

client = discord.Client()

@bot.event
async def on_ready():
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    print('===========================')
    print("{} is now online.".format(bot.user.name))
    print('===========================')
    print("Connected to:")
    print("{} servers".format(servers))
    print("{} channels".format(channels))
    print("{} users".format(users))
    print("=============")
    await bot.change_presence(game=discord.Game(name='with Python'))

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('?hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

'''@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)
'''

@bot.command()
async def ping(response ='Pong!'):
        await bot.say(response)

@bot.command()
async def commands(helpme = "```Current commands are ?roll NdN and ?ping```"):
        await bot.say(helpme)

bot.run('NTM2MzU1MTI4MTQ0NTYwMTM4.DyVfSA.Y0JrNl5-CW67gDHDO_DR1dJ-RbA')
