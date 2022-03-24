from discord.ext import commands

class Music(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def music(self, bot):
    await bot.send("ex-sample")
  
def setup(bot):
  bot.add_cog(Music(bot))