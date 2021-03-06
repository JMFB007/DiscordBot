import os, discord
from discord.ext import commands
from replit import db
import requests
import json
#Colores: 0x9ecdc7 0x007397
class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="Ayuda",aliases=["h","ayuda","aiuda"], brief="Actual help command")
  async def ayuda(self, ctx):#hacer ayuda categoria y comando
    SLUM = os.environ['SLUM']
    if str(ctx.author.id) == str(SLUM):
      embed = discord.Embed(title="**Slum'sMightyBot FULL command list:**", description=f":cyclone: **GENERAL**\n-   Ayuda, Clear, Compliment, Insp.Quote\n:video_game: **FUN**\n-   Random, Roll, Insult\n:musical_note: **MUSIC**\n-   Join, Leave, Play\n:notepad_spiral: **NOTES**\n-   New, Delete, Show\n\n:face_in_clouds: **COMMANDS ONLY <@{SLUM}> CAN USE**\n-   Load, Unload, Reload, FullReload, Databases", color=0x9ecdc7)
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(title="**Slum'sMightyBot FULL command list:**", description=f":cyclone: **GENERAL**\n-   Ayuda, Clear, Compliment, Insp.Quote\n:video_game: **FUN**\n-   Random, Roll, Insult\n:musical_note: **MUSIC**\n-   Join, Leave, Play\n:notepad_spiral: **NOTES**\n-   New, Delete, Show", color=0x9ecdc7)
      await ctx.send(embed=embed)
      
  @commands.command(name="Databases",aliases=["db","databases"], brief="Shows all keys in the Database")
  async def databases(self, ctx):
    if str(ctx.author.id) == str(os.environ['SLUM']):
      s = "**- This are all the keys in the Database:**\n"
      for key in db.keys():
        s += str(key) + "\n"
      await ctx.send(s)
    else:
      await ctx.send(f"<@{ctx.author.id}>, you cant use this command")
  
  @commands.command(name="Clear",aliases=["c", "clear"], brief="Deletes a number of messages")
  async def clear(self, ctx, amount = None):
    try:
      amount = (int(amount)+1)
      await ctx.channel.purge(limit = amount)
    except:
      await ctx.send("Wrong command, please do `-clear #`")
      
  @commands.command(name="Insp.Quote",aliases=["insp", "inspirationalquote"], brief="Shows an inspirational quote")
  async def inspirational_quote(self, ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "*" + json_data[0]["q"].rstrip() + "*" + " - " + json_data[0]["a"]
    await ctx.send(quote)

  @commands.command(name="Compliment",aliases=["comp","compliment"], brief="Shows/sends a compliment")
  async def compliment(self, ctx, arg = None):
    response = requests.get("https://complimentr.com/api")
    json_data = json.loads(response.text)
    if arg == None:
      await ctx.send(json_data["compliment"])
    else:
      await ctx.channel.purge(limit = 1)
      await ctx.send(json_data["compliment"] + " " + arg)
      
  @commands.group(name='Notes',aliases=["notes","n","Note","note"], brief="All note taking commands", invoke_without_command=True)
  async def Notes(self, ctx, arg=None):
    if arg == None:
      await ctx.send("Write `-n new/delete/edit/show` to use the notes")
      Book = db[str(ctx.message.guild.id)]
      s = ""
      for key in Book:
        s += f"**{key}**\n"
      embed = discord.Embed(title="   NOTES:", description=s, color=0x9ecdc7)
      await ctx.send(embed=embed)
    else:
      await ctx.send(f"{arg} is not a subcommand of Notes")

  @Notes.command(name="New",aliases=["new"], brief="Makes a new note")
  async def new(self, ctx, *, arg=None):
    try:
      argt = argn = ""
      arg = arg.split("-",1)
      argt = arg[0].strip()
      argn = arg[1].strip()
    except:
      await ctx.send("Please add the note like this\n`-n new <Title> - <Note>`")
    else:
      if argt == "" or argn == "":
        await ctx.send("Please add the note like this\n`-n new <Title> - <Note>`")
      else:
        Book = db[str(ctx.message.guild.id)]
        flag = True
        for key in Book:
          if str(key) == str(argt):
            flag = False
        if flag:
          db[str(ctx.message.guild.id)][str(argt)] = str(argn)
          await ctx.send("The note has been added!")
          embed = discord.Embed(title=argt, description=db[str(ctx.message.guild.id)][str(argt)], color=0x9ecdc7)
          await ctx.send(embed=embed)
        else:
          await ctx.send("This note already exists, to edit a note do `-n edit <title> - <new note>`")
      
  @Notes.command(name="Delete",aliases=["delete","del"], brief="Deletes a note")
  async def delete(self, ctx, *, key=None):#test
    if key != None:
      Book = db[str(ctx.message.guild.id)]
      s = ""
      for item in Book:
        if str(item) == str(key):
          s = f"Note {key} has been deleted!"
      if s != "":
        await ctx.send(s)
        embed = discord.Embed(title=key, description=Book[str(key)], color=0x9ecdc7)
        await ctx.send(embed=embed)
        del Book[key]
      else:
        await ctx.send(f"Note named {key} doesnt exist")
    else:
      await ctx.send("Please add the title of the note to delete it")

  @Notes.command(name="Edit",aliases=["edit"], brief="Edits a note")
  async def edit(self, ctx, *, key=None):#test
    try:
      argt = argn = ""
      key = key.split("-",1)
      argt = key[0].strip()
      argn = key[1].strip()
    except:
      await ctx.send("Please edit the note like this\n`-n edit <Title> - <new note>`")
    else:
      if argt == "" or argn == "":
        await ctx.send("Please edit the note like this\n`-n edit <Title> - <new note>`")
      else:
        Book = db[str(ctx.message.guild.id)]
        flag = False
        for key in Book:
          if str(key) == str(argt):
            flag = True
        if flag:
          await ctx.send("This is the previous note:")
          embed = discord.Embed(title=argt, description=Book[str(argt)], color=0x9ecdc7)
          await ctx.send(embed=embed)
          Book[str(argt)] = str(argn)
          await ctx.send("The note has been edited!")
          embed = discord.Embed(title=argt, description=Book[str(argt)], color=0x9ecdc7)
          await ctx.send(embed=embed)
        else:
          await ctx.send("This note doesnt exist, to create a new note do `-n new <title> - <Note>`")
  
  @Notes.command(name="Show",aliases=["show"], brief="Shows a specific note")
  async def show(self, ctx, *, arg=None):
    if arg != None:
      Book = db[str(ctx.message.guild.id)]
      embed = None
      for key in Book:
        if str(key) == str(arg):
          embed = discord.Embed(title=key, description=Book[str(key)], color=0x9ecdc7)
      if embed != None:
        await ctx.send(embed=embed)
      else:
        await ctx.send(f"Theres no note named {arg}")
    else:
      await ctx.send("Please add the title of a note to search it")
    
def setup(bot):
  bot.add_cog(General(bot))