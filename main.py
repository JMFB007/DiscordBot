import os
from discord.ext import commands, tasks
from StaynAlive import StaynAlive

bot = commands.Bot(command_prefix = "-")#, help_command=None)

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity="working!")

@bot.command(aliases=["l"], brief="Loads a cog", description="long part")
async def load(ctx, extension):
  try:
    bot.load_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"{extension} is already loaded or doesnt exist")
  else:
    await ctx.send(f"{extension} was loaded")
    
@bot.command(aliases=["u"])
async def unload(ctx, extension):
  try:
    bot.unload_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"{extension} is already unloaded or doesnt exist")
  else:
    await ctx.send(f"{extension} was unloaded")
    
@bot.command(aliases=["r"])
async def reload(ctx, extension):
  try:
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"{extension} doesnt exist")
  else:
    await ctx.send(f"{extension} was reloaded")

@bot.command(aliases=["fr"])
async def fullreload(ctx):
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      bot.unload_extension(f"cogs.{filename[:-3]}")
      bot.load_extension(f"cogs.{filename[:-3]}")
  await ctx.send("All cogs were reloaded!")
  
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")
    
my_secret = os.environ['TOKEN']
StaynAlive()
bot.run(my_secret)