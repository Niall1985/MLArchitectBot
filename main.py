import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from llmbotmodel import bot_response
import asyncio
from flask import Flask
from threading import Thread

load_dotenv()
TOKEN = os.getenv("key")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

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

    try:
        confirm = await interaction.followup.send(f"Cleared {len(deleted)} messages!")
        await asyncio.sleep(2)
        try:
            await confirm.delete()
        except discord.NotFound:
            pass  
    except discord.NotFound:
        pass  


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    if bot.user in message.mentions:
        content = message.content.replace(f"<@{bot.user.id}>", "").strip().lower()
        if content:
            response = await bot_response(content)
            await message.channel.send(response)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

if __name__ == '__main__':
    Thread(target=run_flask).start()
    bot.run(TOKEN)
