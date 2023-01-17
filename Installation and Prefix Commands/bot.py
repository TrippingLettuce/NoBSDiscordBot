import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents) #Commands Prefix can also be ?,.,#,%


#--- Bot Startup
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}') #Bot Name
    print(bot.user.id) #Bot ID

bot.run('TOKEN') #Inster Token ID here should look something like MTA2NDc0NTE3OTAxMTEwODk4Ng.G32ofv...
