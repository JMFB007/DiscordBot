from discord.ext import commands

class Test(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def test2(self, bot):
    await bot.send("test2")

  @commands.command()
  async def wow(self, bot):
    if bot.author == commands.user:
      await bot.send("test")
  
def setup(bot):
  bot.add_cog(Test(bot))