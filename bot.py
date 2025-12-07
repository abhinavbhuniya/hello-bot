import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="hello", description="Say hello to the bot!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! Your bot is active 🎉", ephemeral=True)

bot.run(os.getenv("BOT_TOKEN"))
