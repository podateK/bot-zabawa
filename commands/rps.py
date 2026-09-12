import discord
from discord.ext import commands
import random

class RpsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rps", aliases=["kamien"])
    async def rps(self, ctx, choice: str = None):
        if choice is None:
            await ctx.send("Podaj swój wybór: `?rps kamien`, `?rps papier` lub `?rps nozyce`")
            return

        choices_map = {
            "kamien": "🪨 Kamień",
            "papier": "📄 Papier",
            "nozyce": "✂️ Nożyce"
        }
        bot_choice = random.choice(list(choices_map.keys()))

        choice_lower = choice.lower()
        if choice_lower not in choices_map:
            await ctx.send("Nieprawidłowy wybór! Dostępne: **kamien**, **papier**, **nozyce**")
            return

        if choice_lower == bot_choice:
            result = "Remis! 🤝"
            color = discord.Color.greyple()
        elif (choice_lower == "kamien" and bot_choice == "nozyce") or \
             (choice_lower == "papier" and bot_choice == "kamien") or \
             (choice_lower == "nozyce" and bot_choice == "papier"):
            result = f"Wygrywasz! 🎉 {choices_map[choice_lower]} pokonuje {choices_map[bot_choice]}"
            color = discord.Color.green()
        else:
            result = f"Przegrywasz! 😢 {choices_map[bot_choice]} pokonuje {choices_map[choice_lower]}"
            color = discord.Color.red()

        embed = discord.Embed(title="🎮 Papier, Kamień, Nożyce", color=color)
        embed.add_field(name="Twój wybór", value=choices_map[choice_lower], inline=True)
        embed.add_field(name="Wybór bota", value=choices_map[bot_choice], inline=True)
        embed.add_field(name="Wynik", value=result, inline=False)
        embed.set_footer(text=f"Wywołane przez {ctx.author}", icon_url=ctx.author.display_avatar.url)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(RpsCommand(bot))
