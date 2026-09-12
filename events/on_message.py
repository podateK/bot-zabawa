import discord
from discord.ext import commands

class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        lower = message.content.lower()
        if any(word in lower for word in ["siema", "witam", "cześć", "czesc", "hej"]):
            await message.add_reaction("👋")

async def setup(bot):
    await bot.add_cog(OnMessage(bot))
