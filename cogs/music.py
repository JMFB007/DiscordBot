import discord
from discord.ext import commands
import asyncio
import youtube_dl
import time
from youtube_dl import YoutubeDL

#Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''
#bind to ipv4 since ipv6 addresses cause issues sometimes
ytdl_format_options = {
    'format': 'bestaudio/best',#REMAKE THIS SHIT
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' }

ffmpeg_options = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    'options': '-vn'}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]# take first item from a playlist
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Join",aliases=["join"], brief="Joins your VC")
    async def join(self, ctx):
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            return await ctx.send('You need to be in a voice channel to use this command!')
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
          vc = await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
            vc = ctx.voice_client

    @commands.command(name="Play",aliases=["play"], brief="Plays music in VC")
    async def play(self, ctx):
      if " " not in ctx.message.content:
        await ctx.send("Please add a youtube link play")
      else:
        url = (ctx.message.content).split(" ",1)[1]
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        embed = discord.Embed(title="Now playing", description=f"[{player.title}]({player.url})[{ctx.author.mention}]")
        await ctx.send(embed=embed)

    @commands.command(name="Leave",aliases=["leave","fuck off"], brief="Leaves the VC")
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

intents = discord.Intents.all()
intents.members = True
    
def setup(bot):
  bot.add_cog(Music(bot))