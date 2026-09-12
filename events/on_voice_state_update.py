import discord
from discord.ext import commands

class OnVoiceStateUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if member.bot:
            return

        channel = member.guild.system_channel
        if channel is None:
            return

        if before.channel is None and after.channel is not None:
            await channel.send(f"🎙️ {member.display_name} dołączył/a do kanału głosowego **{after.channel.name}**!")
        elif before.channel is not None and after.channel is None:
            await channel.send(f"🔇 {member.display_name} opuścił/a kanał głosowy **{before.channel.name}**.")
        elif before.channel != after.channel and before.channel is not None and after.channel is not None:
            await channel.send(f"🔄 {member.display_name} przeszedł/a z **{before.channel.name}** do **{after.channel.name}**.")

async def setup(bot):
    await bot.add_cog(OnVoiceStateUpdate(bot))
