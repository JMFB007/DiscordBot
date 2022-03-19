from discord.ext import commands

class Example(commands.Cog):
  
  def __init__(self, bot):
    self.client = bot
  #commands
  @commands.command()
  async def ping(self, ctx):
    await ctx.send("Pong!")
  
def setup(bot):
  bot.add_cog(Example(bot))