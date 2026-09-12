import discord
from discord.ext import commands
import random

class OnMemberRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = member.guild.system_channel
        if channel is None:
            return

        messages = [
            f"{member.display_name} opuścił/a nas... 😢 Będzie brakować!",
            f"Żegnaj {member.display_name}! 🥺 Mamy nadzieję, że wrócisz!",
            f"{member.display_name} właśnie wyszedł/wyszła. Smuteczek. 💔",
            f"Ktoś właśnie opuścił pokój... To był {member.display_name}. 🫡",
            f"{member.display_name} zniknął/zniknął jak magik! 🎩✨"
        ]

        embed = discord.Embed(
            title="👋 Ktoś nas opuścił!",
            description=random.choice(messages),
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Pozostało członków: {member.guild.member_count - 1}")

        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(OnMemberRemove(bot))
