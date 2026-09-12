import discord
from discord.ext import commands
import random

class CoinFlipCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="coinflip", aliases=["rzut", "moneta"])
    async def coinflip(self, ctx):
        result = random.choice(["Orzeł", "Reszka"])
        color = discord.Color.gold() if result == "Orzeł" else discord.Color.blue()
        
        embed = discord.Embed(title="🪙 Rzut monetą", description=f"Wyrzucono: **{result}**!", color=color)
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(CoinFlipCommand(bot))
