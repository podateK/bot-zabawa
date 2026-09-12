import discord
from discord.ext import commands

class OnPresenceUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_presence_update(self, before: discord.Member, after: discord.Member):
        if before.bot:
            return

        channel = before.guild.system_channel
        if channel is None:
            return

        if before.activity != after.activity:
            if after.activity is None and before.activity is not None:
                await channel.send(f"🎮 {after.display_name} przestał/a grać w **{before.activity.name}**.")
            elif after.activity is not None and before.activity is None:
                if after.activity.type == discord.ActivityType.playing:
                    await channel.send(f"🎮 {after.display_name} zaczął/a grać w **{after.activity.name}**!")
                elif after.activity.type == discord.ActivityType.listening:
                    await channel.send(f"🎵 {after.display_name} słucha **{after.activity.name}**.")
                elif after.activity.type == discord.ActivityType.streaming:
                    await channel.send(f"📺 {after.display_name} streamuje **{after.activity.name}**!")

async def setup(bot):
    await bot.add_cog(OnPresenceUpdate(bot))
