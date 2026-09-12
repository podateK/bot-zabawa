import discord
from discord.ext import commands
import random

class JokeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="joke", aliases=["żart", "zart"])
    async def joke(self, ctx):
        jokes = [
            "Dlaczego komputer poszedł do lekarza? Bo miał wirusy!",
            "Co mówi jedna cytryna do drugiej? Nie bądź kwaśny!",
            "Dlaczego programista nosi okulary? Bo nie widzi C#.",
            "Co robi programista, gdy się nudzi? Koduje!",
            "Dlaczego matematyk jest zawsze smutny? Bo ma za dużo problemów.",
            "Jaki jest ulubiony owoc programisty? Kompilator — bo zawsze jest słodki po poprawnym uruchomieniu!",
            "Co mówi jedna płyta CD do drugiej? Zaczekaj, kręcę się!",
            "Dlaczego C++ jest lepszy od C? Bo ma plus za plus!"
        ]
        
        embed = discord.Embed(title="😂 Losowy żart", description=random.choice(jokes), color=discord.Color.gold())
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(JokeCommand(bot))
