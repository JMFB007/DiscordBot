from discord.ext import commands

class Example(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  #events
  @commands.Cog.listener()
  async def on_ready(self):
    print("Bot is online")
  #commands
  @commands.command()
  async def ping(self, ctx):
    await ctx.send("Pong!")
  
def setup(bot):
  bot.add_cog(Example(bot))