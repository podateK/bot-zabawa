import discord
from discord.ext import commands
import random
import re

class RollCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roll", aliases=["rzut"])
    async def roll(self, ctx, dice: str = None):
        if dice is None:
            await ctx.send("Podaj format XdY (np. `?roll 2d6` lub `?roll 1d20`)")
            return

        match = re.match(r"(\d+)d(\d+)", dice.lower())
        if not match:
            await ctx.send("Nieprawidłowy format! Użyj: `?roll XdY` (np. `?roll 2d6`)")
            return

        num_dice = int(match.group(1))
        sides = int(match.group(2))

        if num_dice < 1 or num_dice > 100:
            await ctx.send("Liczba kości musi być między 1 a 100!")
            return
        if sides < 1 or sides > 1000:
            await ctx.send("Liczba ścianek musi być między 1 a 1000!")
            return

        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        total = sum(rolls)
        
        if num_dice == 1:
            description = f"Wyrzucono: **{rolls[0]}**"
        else:
            description = f"Koście: {', '.join(str(r) for r in rolls)}\n**Suma: {total}**"

        embed = discord.Embed(title=f"🎲 Rzut {num_dice}d{sides}", description=description, color=discord.Color.green())
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(RollCommand(bot))
