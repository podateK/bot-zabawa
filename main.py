import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="?", intents=intents)

async def load():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"commands.{filename[:-3]}")
            print(f"Zaladowano komende: {filename}")
    for filename in os.listdir("./events"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"events.{filename[:-3]}")
            print(f"Zaladowano event: {filename}")

@bot.event
async def setup_hook():
    await load()

if __name__ == "__main__":
    if not TOKEN:
        print("Brak DISCORD_TOKEN w pliku .env!")
    else:
        bot.run(TOKEN)
