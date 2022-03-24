import os
from discord.ext import commands#, tasks
from StaynAlive import StaynAlive
#prefix loader
client = commands.Bot(command_prefix = "-")

@client.event#starter message
async def on_ready():
    print("Logged in as {0.user}".format(client))
  
'''@client.command()#test and ping
async def test(ctx):
  await ctx.send(f"ok! ping: {client.latency*1000}ms")'''

@client.command(aliases=["l"])#loads a cog
async def load(ctx, extension):
  try:
    client.load_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"{extension} is already loaded or doesnt exist")
  else:
    await ctx.send(f"{extension} was loaded")
@client.command(aliases=["u"])#unloads a cog
async def unload(ctx, extension):
  try:
    client.unload_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"{extension} is already unloaded or doesnt exist")
  else:
    await ctx.send(f"{extension} was unloaded")
@client.command(aliases=["r"])#reloads a cog
async def reload(ctx, extension):
  try:
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
  except:
    await ctx.send(f"{extension} doesnt exist")
  else:
    await ctx.send(f"{extension} was reloaded")
for filename in os.listdir("./cogs"):#cog loader
  if filename.endswith(".py"):
    client.load_extension(f"cogs.{filename[:-3]}")
    
#things for the client to run
my_secret = os.environ['TOKEN']
StaynAlive()
client.run(my_secret)