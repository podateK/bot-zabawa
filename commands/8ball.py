import discord
from discord.ext import commands
import random

class EightBallCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball")
    async def _8ball(self, ctx, *, question: str = None):
        if not question:
            await ctx.send("Musisz zadać pytanie! Np. `?8ball Czy jutro będzie ładna pogoda?`")
            return
        
        responses = [
            "Tak, zdecydowanie.",
            "Bez wątpienia.",
            "Możesz na to liczyć.",
            "Tak.",
            "Wydaje się to prawdopodobne.",
            "Nie jestem pewien, spróbuj ponownie później.",
            "Lepiej ci teraz nie mówić.",
            "Nie potrafię teraz przewidzieć.",
            "Skoncentruj się i zapytaj ponownie.",
            "Nie licz na to.",
            "Moja odpowiedź brzmi nie.",
            "Moje źródła mówią nie.",
            "Perspektywy nie są zbyt dobre.",
            "Bardzo wątpliwe."
        ]
        
        embed = discord.Embed(title="🎱 Magiczna Kula 8", color=discord.Color.purple())
        embed.add_field(name="Pytanie", value=question, inline=False)
        embed.add_field(name="Odpowiedź", value=random.choice(responses), inline=False)
        embed.set_footer(text=f"Zapytano przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(EightBallCommand(bot))
