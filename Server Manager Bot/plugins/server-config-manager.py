from discord.ext import commands

class Config(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_role("Owner")
    @commands.command()
    async def config(self, ctx, method = "push", *,data = None):
        if data != None or method == "get":
            if method == "push":
                with open("G:\MinecraftServer\plugins\MagicSpells\spells.yml", 'w') as f:
                    file = f.write(data)
                await ctx.send("file has been updated succesfully")
                
            elif method == 'get':
                with open("G:\MinecraftServer\plugins\MagicSpells\spells.yml", 'r') as f:
                    readData = f.read()
                await ctx.send(f'Config\n```{readData}```')
            else:
                await ctx.send("Wrong method please use either `push` to write in config file or `get` to read from config file")

        else:
            await ctx.send("No data has been passed")
            



async def setup(client):
    await client.add_cog(Config(Config))