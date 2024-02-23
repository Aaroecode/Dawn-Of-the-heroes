from discord.ext import commands
import discord

class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client




async def setup(client):
    await client.add_cog(Unban(Unban))