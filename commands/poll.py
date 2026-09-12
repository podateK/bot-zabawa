import discord
from discord.ext import commands
import re

class PollCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="poll", aliases=["ankieta"])
    async def poll(self, ctx, *, question: str = None):
        if question is None:
            await ctx.send("Użycie: `?poll Pytanie | Opcja1 | Opcja2 | Opcja3 ...`")
            return
        
        parts = [p.strip() for p in question.split("|")]
        question_text = parts[0]
        options = parts[1:]

        if len(options) < 2:
            embed = discord.Embed(title="📊 Ankieta", description=question_text, color=discord.Color.blue())
            embed.add_field(name="Reakcje", value="👍 Tak\n👎 Nie", inline=False)
            embed.set_footer(text=f"Ankieta od {ctx.author}", icon_url=ctx.author.display_avatar.url)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
            return

        if len(options) > 9:
            await ctx.send("Możesz dodać maksymalnie 9 opcji!")
            return

        number_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
        
        description = ""
        for i, option in enumerate(options):
            description += f"{number_emojis[i]} {option}\n"

        embed = discord.Embed(title=f"📊 {question_text}", description=description, color=discord.Color.blue())
        embed.set_footer(text=f"Ankieta od {ctx.author}", icon_url=ctx.author.display_avatar.url)
        
        msg = await ctx.send(embed=embed)
        
        for i in range(len(options)):
            await msg.add_reaction(number_emojis[i])

async def setup(bot):
    await bot.add_cog(PollCommand(bot))
