from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ola")
    async def ola(self, ctx):
        await ctx.send(f"Olá {ctx.author.mention}, eu sou um bot!")

    @commands.command(name="soma")
    async def soma(self, ctx, a: int, b: int):
        resultado = a + b
        await ctx.send(f"O resultado de {a} + {b} é {resultado}.")

def setup(bot):
    bot.add_cog(Commands(bot))