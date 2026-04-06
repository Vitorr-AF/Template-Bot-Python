import discord
from discord.ext import commands
from config import TOKEN, PREFIX
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


# Bot online
@bot.event
async def on_ready():
    print(f"{bot.user} está online!")

# Mensagem enviada
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


bot.run(TOKEN)