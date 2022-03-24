from discord.ext import commands
import random

class Dnd(commands.Cog):
  def __init__(self, bot):
    self.client = bot
  #commands
  @commands.command()#-roll 3d20
  async def roll(self, ctx):
    plus = 0
    try:
      times,die = (ctx.message.content).split("d")
      times = int(times[6:])
      if "+" in die:
        die,plus = (die).split("+")
        die = int(die)
        plus = int(plus)
      else:
        die = int(die)
    except:
      await ctx.send("Message sent incorrectly")
    else:
      if (times or die) == None:
        await ctx.send(f"Message sent in an invalid way {times}, {die}")
        pass
      rolls = []
      for n in range(times):
        rolls.append(str(random.randint(1,die)+plus))
      s = "`, `".join(rolls)
      if len(s)>(4000-9):
        await ctx.send("Too many rolls to send")
      else:
        await ctx.send(f"Rolls: `{s}`")
  
def setup(bot):
  bot.add_cog(Dnd(bot))