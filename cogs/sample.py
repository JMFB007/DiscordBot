from discord.ext import commands

class Sample(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def sample(self, bot):
    await bot.send("ex-sample")
  
def setup(bot):
  bot.add_cog(Sample(bot))