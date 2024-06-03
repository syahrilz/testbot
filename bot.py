import discord
from discord.ext import commands
import os
import asyncio
from datetime import datetime, timedelta

# Mengatur intents yang diperlukan
intents = discord.Intents.default()
intents.message_content = True

# Menggunakan commands.Bot alih-alih discord.Client
bot = commands.Bot(command_prefix='$', intents=intents)

start_time = datetime.now()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    try:
        while True:
            if (datetime.now() - start_time) >= timedelta(hours=6):
                print("Bot has been running for 6 hours. Shutting down.")
                await bot.close()
                return

            elapsed_time = datetime.now() - start_time
            elapsed_str = str(elapsed_time).split('.')[0]  # Format: HH:MM:SS
            game = discord.Game(f"Playing a game | {elapsed_str}")
            await bot.change_presence(status=discord.Status.online, activity=game)
            print(f"Updated status: Playing a game | {elapsed_str}")
            await asyncio.sleep(1)  # Update every second
    except Exception as e:
        print(f"An error occurred: {e}")
        await bot.close()
        print("Bot has stopped due to an error")

# Menambahkan perintah ping yang menampilkan latency bot
@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  # Mengubah latency menjadi milidetik
    await ctx.send(f'Pong! {latency:.2f}ms')

# Menambahkan perintah hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

token = os.getenv('DISCORD_TOKEN')
if token is None:
    raise ValueError("DISCORD_TOKEN is not set in environment variables")
bot.run(token)
