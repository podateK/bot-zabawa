import discord
from discord.ext import commands

class HugCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hug", aliases=["przytul"])
    async def hug(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Kogo chcesz przytulić? Podaj użytkownika! Np. `?hug @ktoś`")
            return
        if member == ctx.author:
            await ctx.send("Przytulasz samego siebie? 🫂 Wszyscy potrzebujemy trochę miłości!")
            return

        embed = discord.Embed(
            title="🫂 Przytulanko!",
            description=f"{ctx.author.mention} przytula {member.mention}!",
            color=discord.Color.pink()
        )
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HugCommand(bot))
