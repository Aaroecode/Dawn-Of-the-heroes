from discord.ext import commands
import discord

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.has_permissions(administrator = True)
    @commands.command()
    async def ban(self, ctx, target: discord.Member, *, reason):
        if not target.bot:
            await target.ban(reason=f"User {target.name}#{target.discriminator} has been banned by {ctx.author.name}#{ctx.author.discriminator} for the following reason \n {reason}")
            await ctx.send(f"User {target.name}#{target.discriminator} has been successfully banned")
        else:
            await ctx.send("You can not Ban a bot")


async def setup(client):
    await client.add_cog(Ban(client))