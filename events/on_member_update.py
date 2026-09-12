import discord
from discord.ext import commands

class OnMemberUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        if before.bot:
            return

        channel = before.guild.system_channel
        if channel is None:
            return

        if before.nick != after.nick:
            old_name = before.nick or before.name
            new_name = after.nick or after.name
            embed = discord.Embed(
                title="📝 Zmiana nicku",
                description=f"{after.mention} zmienił/a nick!",
                color=discord.Color.blue()
            )
            embed.add_field(name="Stary nick", value=old_name, inline=True)
            embed.add_field(name="Nowy nick", value=new_name, inline=True)
            embed.set_thumbnail(url=after.display_avatar.url)

            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(OnMemberUpdate(bot))
