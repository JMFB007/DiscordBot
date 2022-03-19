from discord.ext import commands

class Test(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def test(self, client):
    await client.send("test")

  @commands.command()
  async def wow(self, client):
    if client.author == commands.user:
      await client.send("test")
  
def setup(client):
  client.add_cog(Test(client))