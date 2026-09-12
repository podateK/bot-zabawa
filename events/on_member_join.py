import discord
from discord.ext import commands
import random

class OnMemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        welcome_channel = member.guild.system_channel
        if welcome_channel is None:
            return

        messages = [
            f"Hej {member.mention}! Witaj na serwerze! 🎉",
            f"{member.mention} dołączył/a! Wszyscy się cieszą! 🥳",
            f"Nowa osoba! {member.mention}, witamy serdecznie! 👋",
            f"Witaj {member.mention}! Mamy nadzieję, że się dobrze bawić! 🎮",
            f"{member.mention} właśnie wskoczył/a na serwer! Co tu się dzieje! 🚀"
        ]

        embed = discord.Embed(
            title="🎉 Witamy na serwerze!",
            description=random.choice(messages),
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Liczba członków: {member.guild.member_count}")

        await welcome_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(OnMemberJoin(bot))
