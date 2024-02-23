from discord.ext import commands
import discord

class Avatar(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
    
    @commands.command
    async def avatar(self, ctx, user: discord.Member = None):
        if user is None:
            user =  ctx.author
        avatarLink = user.avatar.url

        avatarEmbed = discord.Embed(
            title = f"The Avatar of {user.display_name}"
        )
        await ctx.send(Embed=avatarEmbed)


async def setup(client):
    await client.add_cog(Avatar(Avatar))