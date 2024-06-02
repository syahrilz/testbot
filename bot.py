import discord
import os
import asyncio
from datetime import datetime

# Mengatur intents yang diperlukan
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

start_time = datetime.now()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    game = discord.Game(f"Playing a game | {datetime.now().strftime('%H:%M:%S')}")
    await client.change_presence(status=discord.Status.online, activity=game)

    while True:
        elapsed_time = datetime.now() - start_time
        elapsed_str = str(elapsed_time).split('.')[0]  # Format: HH:MM:SS
        game = discord.Game(f"Playing a game | {elapsed_str}")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)  # Update every 10 seconds

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
