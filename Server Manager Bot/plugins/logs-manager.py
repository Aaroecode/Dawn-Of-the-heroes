from discord.ext import commands

class logs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_role("Owner")
    @commands.command()
    async def logs(self, ctx):
        with open("G:\MinecraftServer\logs\latest.log", "r") as f:
            log = f.read()
        await ctx.send(log)

async def setup(client):
    await client.add_cog(logs(logs))