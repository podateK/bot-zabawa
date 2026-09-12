import discord
from discord.ext import commands

class SlapCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="slap", aliases=["plask"])
    async def slap(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Kogo chcesz spłaszczyć? Podaj użytkownika! Np. `?slap @ktoś`")
            return
        if member == ctx.author:
            await ctx.send("Uderzasz samego siebie?! 😵 Potrzebujesz pomocy!")
            return

        embed = discord.Embed(
            title="👋 Plask!",
            description=f"{ctx.author.mention} daje plask {member.mention}!",
            color=discord.Color.orange()
        )
        embed.add_field(name="Efekt", value="Zostawiło to ślad!", inline=False)
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(SlapCommand(bot))
