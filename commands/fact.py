import discord
from discord.ext import commands
import random

class FactCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fact", aliases=["ciekawostka"])
    async def fact(self, ctx):
        facts = [
            "Bananowce to tak naprawdę ogromne zioła, a nie drzewa.",
            "Ośmiornice mają trzy serca i niebieską krew.",
            "Pszczoły potrafią rozpoznać ludzkie twarze.",
            "Serce krewetki znajduje się w jej głowie.",
            "Krowy mają najlepszych przyjaciół i stresują się, gdy są od nich oddzielane.",
            "Większość ludzi nie może dotknąć łokciem własnego języka.",
            "Kot spędza średnio 70% swojego życia na śpaniu.",
            "Wulkany na Wenus są liczniejsze niż na jakiejkolwiek innej planecie Układu Słonecznego."
        ]
        
        embed = discord.Embed(title="💡 Losowa ciekawostka", description=random.choice(facts), color=discord.Color.teal())
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(FactCommand(bot))
