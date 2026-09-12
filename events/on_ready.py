import discord
from discord.ext import commands

class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot zalogowany jako {self.bot.user} (ID: {self.bot.user.id})")
        print(f"Liczba serwerów: {len(self.bot.guilds)}")
        
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="?help | Zabawa!"
            )
        )

async def setup(bot):
    await bot.add_cog(OnReady(bot))
