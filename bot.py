import os
import discord
from discord.ext import tasks, commands

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    send_message.start()

@tasks.loop(minutes=10)
async def send_message():
    channel = bot.get_channel(int(CHANNEL_ID))
    if channel:
        await channel.send("Hello! This message is sent every 10 minutes.")

@send_message.before_loop
async def before_send_message():
    await bot.wait_until_ready()

bot.run(TOKEN)
