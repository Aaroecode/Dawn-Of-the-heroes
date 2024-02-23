from discord.ext import commands
from pyngrok import ngrok as angrok
import discord, os, dotenv, utility.ngrok as ngrok
import utility.server as server
import subprocess, asyncio, functools
dotenv.load_dotenv()





channel_id = int(os.getenv("STATUS_CHANNLE_ID"))
message_id = int(os.getenv("SERVER_STATUS_MESSAGE_ID"))

class start(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.has_role("Owner")    
    @commands.command()
    async def start(self, ctx):
        channel = discord.utils.get(ctx.guild.channels, id = channel_id)
        message = await channel.fetch_message(message_id)
        ssh = ngrok.run()
        server_status_embed  = discord.Embed(title=f"*Current Server Status*",description="Online ✅", color=discord.Color.green())
        server_status_embed.add_field(name="IP of Server", value=f'`{str(ssh)[20:-22]}`', inline=False)
        server_status_embed.add_field(name= "Server Mode", value="Development", inline=False)
        server_status_embed.set_thumbnail(url="https://www.pngfind.com/pngs/m/0-226_image-checkmark-green-check-mark-circle-hd-png.png")
        await message.edit(embed = server_status_embed)
        await server.start()
    

    @commands.has_role("Owner")
    @commands.command()
    async def stop(self, ctx):
        os.system("taskkill/im java.exe")
        angrok.kill()
        channel = discord.utils.get(ctx.guild.channels, id = channel_id)
        message = await channel.fetch_message(message_id)

        server_status_embed  = discord.Embed(title=f"*Current Server Status*",description="Offline ❎", color=discord.Color.red())
        server_status_embed.add_field(name="IP of Server", value=f'`No IP Found`', inline=False)
        server_status_embed.add_field(name= "Server Mode", value="Development", inline=False)
        server_status_embed.set_thumbnail(url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-9OVBCz0oVCfHYF93BBV4FKGZEES_59TG3w&usqp=CAU")
        await message.edit(embed = server_status_embed)

        




async def setup(client):
    await client.add_cog(start(start))