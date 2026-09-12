import discord
from discord.ext import commands

class OnGuildChannelDelete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        guild_channel = channel.guild.system_channel
        if guild_channel is None:
            return

        embed = discord.Embed(
            title="🗑️ Usunięty kanał",
            description=f"Usunięto kanał: **{channel.name}**",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Serwer: {channel.guild.name}")

        await guild_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(OnGuildChannelDelete(bot))
