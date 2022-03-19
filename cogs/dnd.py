from discord.ext import commands
import random

class Dnd(commands.Cog):
  def __init__(self, bot):
    self.client = bot
  #commands
  @commands.command()#-roll 10d20
  async def roll(self, ctx):
    try:
      times,die = (ctx.message.content).split("d")
      times = int(times[6:])
      die = int(die)
    except:
      await ctx.send("Message sent incorrectly")
    else:
      if (times or die) == None:
        await ctx.send(f"Message sent in an invalid way {times}, {die}")
        pass
      print(str(times) + "," + str(die))
      rolls = []
      for n in range(times):
        rolls.append(str(random.randint(1,die)))
      s = "`, `".join(rolls)
      await ctx.send(f"Rolls: `{s}`")
  
def setup(bot):
  bot.add_cog(Dnd(bot))