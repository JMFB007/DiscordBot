import discord
from discord.ext import commands
import asyncio
import youtube_dl

class Music(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.queue = {}
    '''self.setup()
  
  def setup(self):
    for guild in self.bot.guilds:
      self.song_queue[guild.id] = []

  async def check_queue(self,ctx):
    if len(self.song_queue[ctx.guild.id]) > 0:
      ctx.voice_client.stop()
      await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
      self.song_queue[ctx.guild.id].pop(0)
      
  async def play_song(self, ctx, song):
    url = pafy.new(song).getbestaudio().url
    ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
    ctx.voice_client.source.volume = 0.5

  @commands.command(name="Play", aliases=["play"], brief="Plays a youtube video")
  async def play(self, ctx, *, song=None):
    if song is None:
        return await ctx.send("Gotta tell me what to play before I can bust out the music")
    if ctx.voice_client is None:
        return await ctx.send("Come on bud, why would I sing my tunes if you're not even listening!?")
    if not("youtube.com/watch?" in song or "https:youtu.be/" in song):
      await ctx.send("Searching for song, gonna have to wait a sec")
      result = await self.search_song(1, song, get_url=True)
      if result is None:
          return await ctx.send("Are you sure this is really a song? Maybe try search for it with my command, =play insert song name here")
      song = result[0]
      
    if ctx.voice_client.source is not None:
      queue_len = len(self.song_queue[ctx.guild.id])
      self.song_queue[ctx.guild.id].append(song)
      return await ctx.send(f"The song's been added to your queue, position {queue_len+1}.")

    try:
      await self.play_song(ctx, song)
    except:
      queue_len = len(self.song_queue[ctx.guild.id])
      self.song_queue[ctx.guild.id].append(song)
      return await ctx.send(f"I don't think you can listen to two songs at once. The song's been added to your queue, position {queue_len+1}.")'''
    
def setup(bot):
  bot.add_cog(Music(bot))