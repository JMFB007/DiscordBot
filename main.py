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
  
#cog loader
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    client.load_extension(f"cogs.{filename[:-3]}")
#things for the client to run
my_secret = os.environ['TOKEN']
StaynAlive()
client.run(my_secret)