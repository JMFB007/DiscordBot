import os, discord
from discord.ext import commands, tasks
from replit import db
from StaynAlive import StaynAlive

bot = commands.Bot(command_prefix = "-")#, help_command=None)
SLUM = os.environ['SLUM']

@bot.event
async def on_ready():
  print("Logged in as: {0.user}".format(bot))
  change_status.start()

@tasks.loop(seconds=3600)
async def change_status():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your orders!"))

@bot.event
async def on_guild_join(guild):
  db[str(guild.id)] = {"Note":"This is a note"}
  
@bot.event
async def on_guild_remove(guild):
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="left server!"))
  del db[str(guild.id)]

@bot.command(name="Load",aliases=["l","load"], brief="Loads a cog")
async def load(ctx, extension):
  if str(ctx.author.id) == str(SLUM):
    try:
      bot.load_extension(f"cogs.{extension}")
    except:
      await ctx.send(f"{extension} is already loaded or doesnt exist")
    else:
      await ctx.send(f"{extension} was loaded")
  else:
    await ctx.send(f"{ctx.author.id}, you cant use this command")
    
@bot.command(name="Unload",aliases=["u","unload"], brief="Unloads a cog")
async def unload(ctx, extension):
  if str(ctx.author.id) == str(SLUM):
    try:
      bot.unload_extension(f"cogs.{extension}")
    except:
      await ctx.send(f"{extension} is already unloaded or doesnt exist")
    else:
      await ctx.send(f"{extension} was unloaded")
  else:
    await ctx.send(f"{ctx.author.id}, you cant use this command")
    
@bot.command(name="Reload",aliases=["r","reload"], brief="Reloads a cog")
async def reload(ctx, extension):
  if str(ctx.author.id) == str(SLUM):
    try:
      bot.unload_extension(f"cogs.{extension}")
      bot.load_extension(f"cogs.{extension}")
    except:
      await ctx.send(f"{extension} doesnt exist")
    else:
      await ctx.send(f"{extension} was reloaded")
  else:
    await ctx.send(f"{ctx.author.id}, you cant use this command")

@bot.command(name="FullReload",aliases=["fr","fullreload"], brief="Reloads ALL cogs")
async def full_reload(ctx):
  if str(ctx.author.id) == str(SLUM):
    for filename in os.listdir("./cogs"):
      if filename.endswith(".py"):
        bot.unload_extension(f"cogs.{filename[:-3]}")
        bot.load_extension(f"cogs.{filename[:-3]}")
    await ctx.send("All cogs were reloaded!")
  else:
    await ctx.send(f"<@{ctx.author.id}>, you cant use this command")

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")
    
BotToken = os.environ['TOKEN']
StaynAlive()
bot.run(BotToken)