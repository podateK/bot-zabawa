import discord
from discord.ext import commands
import random

class MemeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="meme", aliases=["memy"])
    async def meme(self, ctx):
        memes = [
            "Gdy piszesz kod bez błędów, ale on i tak nie działa.",
            "Ja: Muszę iść spać. Też ja: Jeszcze tylko jeden commit.",
            "Programista: To działa na mojej maszynie.",
            "Gdy produktownik mówi 'to zajmie 5 minut'.",
            "Stack Overflow: Twoje ulubione źródło odpowiedzi.",
            "Kiedy bug znika po dodaniu jednej linii komentarza.",
            "Gdy kompilator mówi '1 error', a ty masz 500 linii kodu.",
            "DevOps: Wszystko w porządku. *Serwer się pali* Wszystko w porządku."
        ]
        
        embed = discord.Embed(title="🐸 Losowy mem", description=random.choice(memes), color=discord.Color.dark_purple())
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(MemeCommand(bot))
