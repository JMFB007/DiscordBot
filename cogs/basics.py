import discord
from discord.ext import commands
from discord.utils import get
import requests
import json

class Basics(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=["h"])
  async def ayuda(self, ctx):
    slum = 588231330924593164
    if ctx.author.id == slum:
      embed = discord.Embed(title="HELP", description=f"wanana banana\nxd \n\n<@{slum}>:sunglasses:")
      await ctx.send(embed=embed)
    else:
      await ctx.send("*cursiva* **negrita** ***cursiva negrita*** __subrayado__ `linea de codigo` ```multilinea de codigo``` >>> normal con linea a la izq")
  
  @commands.command(aliases=["c"])
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
  bot.add_cog(Basics(bot))