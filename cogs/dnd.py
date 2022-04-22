from discord.ext import commands
import random

class Dnd(commands.Cog):
  def __init__(self, bot):
    self.client = bot
    
  @commands.command(name="Roll", aliases=["roll"], brief="Rolls a dice")
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

  @commands.command(name="Random", aliases=["random"], brief="Shows a random number between 2")
  async def random(self, ctx):
    r = ctx.message.content[6:]
    n = 0
    while r[n].isdigit():
      n += 1
    if n == 0:
      return "ERRORnum"
    a = r[0:(n-len(r))]
    if not(r[n] == "-"):
      return "ERROR"
    r = r[n+1:]
    n = 0
    while r[n].isdigit() and r[n] != None:
      n += 1
    if n == 0:
      return r[n] + "lol"
    b = r[0:(n-len(r))]
    if int(a)<int(b):
      return "ERROR"
    else:
      return random.randint(int(a),int(b))
  
def setup(bot):
  bot.add_cog(Dnd(bot))