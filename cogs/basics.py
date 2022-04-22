import discord
import os
from discord.ext import commands
from replit import db
#import AsyncDatabase from replit.database
#from discord.utils import get
import requests
import json

class Basics(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="Ayuda",aliases=["h","ayuda","aiuda"], brief="Actual help command")
  async def ayuda(self, ctx):
    SLUM = os.environ['SLUM']
    if str(ctx.author.id) == str(SLUM):
      embed = discord.Embed(title="LIST OF COMPLETE COMMANDS", description=f"BASICS: Ayuda, Clear, Compliment, Insp.Quote\nDND: Random, Roll\nFUN: Insult\nMUSIC: Join, Leave, Play\n\nCOMMANDS ONLY <@{SLUM}> CAN USE:\nLoad, Unload, Reload, FullReload")
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(title="List of Commands", description=f"BASICS: Ayuda, Clear, Compliment, Insp.Quote\nDND: Random, Roll\nFUN: Insult\nMUSIC: Join, Leave, Play")
      await ctx.send(embed=embed)
  
  @commands.command(name="Clear",aliases=["c"], brief="Deletes a number of messages")
  async def clear(self, ctx, amount=1):
    await ctx.channel.purge(limit = (amount+1))
  
  @commands.command(name="Insp.Quote",aliases=["insp", "inspirational quote"], brief="Shows an inspirational quote")
  async def inspirational_quote(self, ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "*" + json_data[0]["q"].rstrip() + "*" + " - " + json_data[0]["a"]
    await ctx.send(quote)

  @commands.command(name="Compliment",aliases=["comp","compliment"], brief="Shows/sends a compliment")
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

  @commands.group(name='Notes',aliases=["notes","n"], brief="All note taking commands", invoke_without_command=True)
  async def Notes(self, ctx, arg=None):
    if arg == None:
      await ctx.send("Write `-n new/del/show` to use the notes")
      Book = db[str(ctx.message.guild.id)]
      s = ""
      for key in Book:
        s += f"**{key}**\n"
      embed = discord.Embed(title="   NOTES:", description=s)
      await ctx.send(embed=embed)
    else:
      await ctx.send(f"{arg} is not a subcommand of Notes")

  @Notes.command(name="New",aliases=["new"], brief="Makes a new note")
  async def new(self, ctx, argt=None, argn=None):
    if argt != None and argn != None:
      db[str(ctx.message.guild.id)][str(argt)] = str(argn)
      await ctx.send("The note has been added!")
      embed = discord.Embed(title=argt, description=db[str(ctx.message.guild.id)][str(argt)])
      await ctx.send(embed=embed)
    else:
      await ctx.send("Please add the title of the note and its contents to make a new note")
      
  @Notes.command(name="Delete",aliases=["delete","del"], brief="Deletes a note")
  async def delete(self, ctx, argt=None):
    if argt != None:
      Book = db[str(ctx.message.guild.id)]
      s = ""
      for key in Book:
        if str(key) == str(argt):
          s = f"Note {argt} has been deleted!"
      if s != "":
        del Book[argt]
        await ctx.send(s)
      else:
        await ctx.send(f"Note named {argt} doesnt exist")
    else:
      await ctx.send("Please add the title of the note to delete it")
    
  @Notes.command(name="Show",aliases=["show"], brief="Shows a specific note")
  async def show(self, ctx, arg=None):
    if arg != None:
      Book = db[str(ctx.message.guild.id)]
      embed = None
      for key in Book:
        if str(key) == str(arg):
          embed = discord.Embed(title=key, description=Book[str(key)])
      if embed != None:
        await ctx.send(embed=embed)
      else:
        await ctx.send(f"Theres no note named {arg}")
    else:
      await ctx.send("Please add the title of a note to search it")
    
def setup(bot):
  bot.add_cog(Basics(bot))