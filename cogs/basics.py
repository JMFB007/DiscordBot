import discord
import os
from discord.ext import commands
#from discord.utils import get
import requests
import json

class Basics(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="aiuda",aliases=["h"])
  async def ayuda(self, ctx):
    SLUM = os.environ['SLUM']
    if ctx.author.id == SLUM:
      embed = discord.Embed(title="LIST OF COMPLETE COMMANDS", description=f"BASICS: ayuda, clear, compliment, inspirational_quote\nDND: random, roll\nFUN: insulto\nMUSIC: join, leave, play\n\nCOMMANDS ONLY <@{SLUM}> CAN USE:\nload, unload, reload, full_reload")
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(title="List of Commands", description=f"BASICS: ayuda, clear, compliment, inspirational_quote\nDND: random, roll\nFUN: insulto\nMUSIC: join, leave, play")
      await ctx.send(embed=embed)
  
  @commands.command(aliases=["c"])
  async def clear(self, ctx, amount=1):
    await ctx.channel.purge(limit = (amount+1))
  
  @commands.command(aliases=["insp"])
  async def inspirational_quote(self, ctx):
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
  bot.add_cog(Basics(bot))