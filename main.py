import discord
from discord.ext import commands
import os
import time
from replit import db


import dnd
import other
from StaynAlive import StaynAlive

#joke, snake, card and dice games, be on github, bandera check
#poggers poggers 

my_secret = os.environ['TOKEN']
client = discord.Client()
creep = ["creeper","Creeper"]
pog = ["Pog","pog","Poggers","poggers"]

@client.event
async def on_ready():
  print("IT'S ON! {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content

  help = ">>> say creeper or pog hard to meme\nList of commands:\n `$joke`,`$insult`,`$inspire`,`$critsucc`,`$critfail`,`$rando`#`-`#\nROLLS:\n `$roll`roll #`d`dice # (DICES: 2,4,6,8,10,12,20)"
  if msg == "$help":
    await message.channel.send(help)
  if msg.startswith("$roll"):
    await message.channel.send(dnd.roll(msg))
  if msg.startswith("$crit"):
    await message.channel.send(dnd.crit(msg))
  if msg.startswith("$rando"):
    await message.channel.send(other.rando(msg))
  if msg.startswith("$joke"):
    await message.channel.send("Why did the blind man fall into the well?\nBecause he couldnt see that well!:rofl:")
  if msg.startswith("$inspire"):
    await message.channel.send(other.get_quote())
  if msg.startswith("$t"):
    time.sleep(10)
    await message.author.send('Hello World!')#send dm
  if msg.startswith("$insult"):
    at = msg[8:]
    if at == "":
      await message.channel.send("Oiga...pero quien es el pinche pendejo que voy a insultar we?\n Pongalo con asi: `$insulto @*persona*`")
    else:
      n=4
      await message.channel.send(other.insult() + at)
      while n>0:
        time.sleep(10)
        await message.channel.send(other.insult() + at)
        n-=1
  if msg.startswith("$add "):
    txt = msg.split("$add ",1)[1]
    db["aa"] = txt
    await message.channel.send(f"{txt} was added")
  if msg.startswith("$show"):
    txt = ""
    for key in db.keys():
      txt += key + "   "
    await message.channel.send(txt)
  if msg.startswith("$delete"):
    for key in db.keys():
      txt = db[key]
      del db[key]
      await message.channel.send(f"{txt} was deleted")
  if any(word in msg for word in creep):
    await message.channel.send("AW MAN")
  if any(word in msg for word in pog):
    await message.channel.send("https://tenor.com/view/poggers-pepe-gif-12187647")

StaynAlive()
client.run(my_secret)