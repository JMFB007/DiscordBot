import os
import discord
from discord.ext import commands, tasks
from StaynAlive import StaynAlive

bot = commands.Bot(command_prefix = "-")#, help_command=None)

@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))
  change_status.start()

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your orders!"))

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