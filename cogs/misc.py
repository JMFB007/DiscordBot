from discord.ext import commands
import requests
import json

class Misc(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def clear(self, ctx, amount=1):
    await ctx.channel.purge(limit = (amount+1))
  
  @commands.command(aliases=["insp"])
  async def inspquote(self, ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "*" + json_data[0]["q"].rstrip() + "*" + " - " + json_data[0]["a"]
    await ctx.send(quote)

  @commands.command(aliases=["comp"])
  async def compliment(self, ctx):
    if " " in ctx.message.content:
      member = (ctx.message.content).split(" ")[-1]
    else:
      member = ""
    response = requests.get("https://complimentr.com/api")
    json_data = json.loads(response.text)
    quote = json_data["compliment"] + " " + member
    if member != "":
      await ctx.channel.purge(limit = 1)
    await ctx.send(quote)
  
def setup(bot):
  bot.add_cog(Misc(bot))