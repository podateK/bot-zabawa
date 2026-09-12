import discord
from discord.ext import commands

class OnCommandError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("🤔 Nie znam tej komendy! Użyj `?help` aby zobaczyć dostępne komendy.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"❌ Brakuje argumentu: **{error.param.name}**. Użyj `?help {ctx.command}` aby zobaczyć jak użyć tej komendy.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("❌ Podano nieprawidłowy argument! Sprawdź format i spróbuj ponownie.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("🚫 Nie masz uprawnień do tej komendy!")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("🤖 Bot nie ma wystarczających uprawnień do wykonania tej komendy!")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"⏳ Ta komenda jest na cooldownie! Spróbuj ponownie za {error.retry_after:.1f} sekund.")
        else:
            await ctx.send("❌ Wystąpił nieoczekiwany błąd! Spróbuj ponownie później.")
            raise error

async def setup(bot):
    await bot.add_cog(OnCommandError(bot))
