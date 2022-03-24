from discord.ext import commands

class Fun(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def fun(self, bot):
    await bot.send("ex-sample")
  
def setup(bot):
  bot.add_cog(Fun(bot))