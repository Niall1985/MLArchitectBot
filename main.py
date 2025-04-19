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
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)
tree = bot.tree  
@bot.event
async def on_ready():
    await tree.sync() 
    print(f'Bot is online as {bot.user}')


@tree.command(name="clear", description="Clear messages from the channel")
@discord.app_commands.describe(amount="Number of messages to delete (default 100)")
async def clear(interaction: discord.Interaction, amount: int = 100):
   
    if not interaction.channel.permissions_for(interaction.user).manage_messages:
        await interaction.response.send_message("You don't have permission to manage messages.", ephemeral=True)
        return

    await interaction.response.defer()
    deleted = await interaction.channel.purge(limit=amount)
    confirm = await interaction.followup.send(f"Cleared {len(deleted)} messages!")
    await asyncio.sleep(2)
    await confirm.delete()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)  
    if message.content.startswith('/'):
        return  

    content = message.content.lower()
    response = await bot_response(content)
    await message.channel.send(response)

bot.run(TOKEN)
