import discord
from discord.ext import commands

#---Other Imports
import tok

TOKEN = tok.token

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#--- Bot Startup
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}') #Bot Name
    print(bot.user.id) #Bot ID

bot.run(TOKEN)
