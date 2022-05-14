import asyncio
import discord
from discord.ext.commands import *
import cleverbotfree
from keys import USER_TOKEN

token = USER_TOKEN
prefix = '!'
intents = discord.Intents(messages=True, members=True)

client = Bot(command_prefix=prefix, self_bot=True, intents=intents)
client.remove_command('help')

async def async_chat(message):
    """Example code using cleverbotfree async api."""
    async with cleverbotfree.async_playwright() as p_w:
        c_b = await cleverbotfree.CleverbotAsync(p_w)
        user_input = message
        bot = await c_b.single_exchange(user_input)
        await c_b.close()
        return bot

@client.event
async def on_ready():
    """triggers when bot is running"""
    await client.change_presence(status=discord.Status.online)
    print('Selfbot is ready!')

@client.listen('on_message')
async def on_message(message):
    """respond to messages"""
    if message.author == client.user:
        return
    else:
        response = await async_chat(message.content)
        await message.channel.send(response)

client.run(token, bot=False)
