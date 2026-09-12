import discord
from discord.ext import commands

class PatCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pat", aliases=["pogłaszcz"])
    async def pat(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Kogo chcesz pogłaskać? Podaj użytkownika! Np. `?pat @ktoś`")
            return
        if member == ctx.author:
            await ctx.send("Pogłaskujesz samego siebie? 🥺 Jesteś sobie wystarczający!")
            return

        embed = discord.Embed(
            title="🤚 Pogłaskanko!",
            description=f"{ctx.author.mention} pogłaskuje {member.mention} po głowie!",
            color=discord.Color.blurple()
        )
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(PatCommand(bot))
