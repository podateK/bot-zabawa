import discord
from discord.ext import commands

class OnReactionAdd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.User):
        if user.bot:
            return

        if reaction.count >= 3:
            await reaction.message.channel.send(
                f"Reakcja {reaction.emoji} osiągnęła 3+ reakcji na wiadomości od {reaction.message.author.display_name}!"
            )

async def setup(bot):
    await bot.add_cog(OnReactionAdd(bot))
