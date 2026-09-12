import discord
from discord.ext import commands

class KissCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kiss", aliases=["całuj"])
    async def kiss(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Kogo chcesz pocałować? Podaj użytkownika! Np. `?kiss @ktoś`")
            return
        if member == ctx.author:
            await ctx.send("Próbujesz pocałować samego siebie? 😘 Niezły popis!")
            return

        embed = discord.Embed(
            title="😘 Buśka!",
            description=f"{ctx.author.mention} daje buśka {member.mention}!",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(KissCommand(bot))
