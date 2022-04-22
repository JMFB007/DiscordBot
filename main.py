import os
<<<<<<< HEAD
import discord
from discord.ext import commands, tasks
=======
from replit import db

>>>>>>> origin/main
from StaynAlive import StaynAlive

bot = commands.Bot(command_prefix = "-")#, help_command=None)

<<<<<<< HEAD
@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))
  change_status.start()

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your orders!"))
=======
my_secret = os.environ['TOKEN']
client = discord.Client()
creep = ["creeper","Creeper"]
pog = ["Pog","pog","Poggers","poggers"]

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
>>>>>>> origin/main

SLUM = os.environ['SLUM']
    
@bot.command(aliases=["l"], brief="Loads a cog", description="long part")
async def load(ctx, extension):
  if ctx.author.id == SLUM:
    try:
      bot.load_extension(f"cogs.{extension}")
    except:
      await ctx.send(f"{extension} is already loaded or doesnt exist")
    else:
      await ctx.send(f"{extension} was loaded")
  else:
    await ctx.send(f"{ctx.author.id}, you cant use this command")
    
@bot.command(aliases=["u"])
async def unload(ctx, extension):
  if ctx.author.id == SLUM:
    try:
      bot.unload_extension(f"cogs.{extension}")
    except:
      await ctx.send(f"{extension} is already unloaded or doesnt exist")
    else:
<<<<<<< HEAD
      await ctx.send(f"{extension} was unloaded")
  else:
    await ctx.send(f"{ctx.author.id}, you cant use this command")
    
@bot.command(aliases=["r"])
async def reload(ctx, extension):
  if ctx.author.id == SLUM:
    try:
      bot.unload_extension(f"cogs.{extension}")
      bot.load_extension(f"cogs.{extension}")
    except:
      await ctx.send(f"{extension} doesnt exist")
    else:
      await ctx.send(f"{extension} was reloaded")
  else:
    await ctx.send(f"{ctx.author.id}, you cant use this command")

@bot.command(aliases=["fr"])
async def full_reload(ctx):
  if ctx.author.id == SLUM:
    for filename in os.listdir("./cogs"):
      if filename.endswith(".py"):
        bot.unload_extension(f"cogs.{filename[:-3]}")
        bot.load_extension(f"cogs.{filename[:-3]}")
    await ctx.send("All cogs were reloaded!")
  else:
    await ctx.send(f"{ctx.author.id}, you cant use this command")

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")
    
BotToken = os.environ['TOKEN']
StaynAlive()
bot.run(BotToken)
=======
      n=4
      await message.channel.send(other.insult() + at)
      while n>0:
        time.sleep(10)
        await message.channel.send(other.insult() + at)
        n-=1
  if msg.startswith("$add "):
    txt = msg.split("$add ",1)[1]
    db["aa"] = txt
    await message.channel.send(f"{txt} was added")
  if msg.startswith("$show"):
    txt = ""
    for key in db.keys():
      txt += key + "   "
    await message.channel.send(txt)
  if msg.startswith("$delete"):
    for key in db.keys():
      txt = db[key]
      del db[key]
      await message.channel.send(f"{txt} was deleted")
  if any(word in msg for word in creep):
    await message.channel.send("AW MAN")
  if any(word in msg for word in pog):
    await message.channel.send("https://tenor.com/view/poggers-pepe-gif-12187647")
>>>>>>> origin/main
