import discord
from discord.ext import commands
import random

class DiceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dice", aliases=["kostka"])
    async def dice(self, ctx, sides: int = 6):
        if sides < 2:
            await ctx.send("Kostka musi mieć przynajmniej 2 ścianki!")
            return
        
        result = random.randint(1, sides)
        embed = discord.Embed(title="🎲 Rzut kością", description=f"Wyrzucono **{result}** (z {sides} ścianek)!", color=discord.Color.green())
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(DiceCommand(bot))
