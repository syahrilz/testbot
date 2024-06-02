import discord
import os
import asyncio
from datetime import datetime, timedelta

# Mengatur intents yang diperlukan
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

start_time = datetime.now()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    while (datetime.now() - start_time) < timedelta(hours=6):
        elapsed_time = datetime.now() - start_time
        elapsed_str = str(elapsed_time).split('.')[0]  # Format: HH:MM:SS
        game = discord.Game(f"Playing a game | {elapsed_str}")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(1)  # Update every second
    await client.close()
    print("Bot has stopped after 6 hours")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

token = os.getenv('DISCORD_TOKEN')
if token is None:
    raise ValueError("DISCORD_TOKEN is not set in environment variables")
client.run(token)
