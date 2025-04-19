import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from llmbotmodel import bot_response
import asyncio
load_dotenv()
TOKEN = os.getenv("key")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), case_insensitive=True)

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 100):
    await ctx.channel.purge(limit=amount)
    confirmation = await ctx.send(f"Cleared {amount} messages!")
    await asyncio.sleep(2)
    await confirmation.delete()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)  
    if message.content.startswith('!'):
        return
    content = message.content.lower()
    response = await bot_response(content)
    await message.channel.send(response)

bot.run(TOKEN)
