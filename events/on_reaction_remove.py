import discord
from discord.ext import commands

class OnReactionRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction: discord.Reaction, user: discord.User):
        if user.bot:
            return

        print(f"{user.display_name} usunął reakcję {reaction.emoji} z wiadomości na serwerze {reaction.message.guild.name}")

async def setup(bot):
    await bot.add_cog(OnReactionRemove(bot))
