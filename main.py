import os
from discord.ext import commands#, tasks
from StaynAlive import StaynAlive
#prefix loader
client = commands.Bot(command_prefix = "-")
#starter message
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
  
#test and ping
@client.command()
async def test(ctx):
  await ctx.send(f"ok! ping: {client.latency*1000}ms")
#loads a cog
@client.command()
async def load(ctx, extension):
  try:
    client.load_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"{extension} is already loaded or doesnt exist")
  else:
    await ctx.send(f"{extension} was loaded")
#unloads a cog
@client.command()
async def unload(ctx, extension):
  try:
    client.unload_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"{extension} is already unloaded or doesnt exist")
  else:
    await ctx.send(f"{extension} was unloaded")
#reloads a cog
@client.command()
async def reload(ctx, extension):
  try:
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"{extension} doesnt exist")
  else:
    await ctx.send(f"{extension} was reloaded")
#cog loader
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    client.load_extension(f"cogs.{filename[:-3]}")
#things for the client to run
my_secret = os.environ['TOKEN']
StaynAlive()
client.run(my_secret)