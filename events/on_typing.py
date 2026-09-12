import discord
from discord.ext import commands

class OnTyping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        if user.bot:
            return

        if isinstance(channel, discord.TextChannel):
            print(f"{user.display_name} pisze w #{channel.name} na serwerze {channel.guild.name}")

async def setup(bot):
    await bot.add_cog(OnTyping(bot))
