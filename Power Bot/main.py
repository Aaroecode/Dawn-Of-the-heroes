from discord.ext import commands
from datetime import datetime
from dotenv import load_dotenv
import discord, os, json

load_dotenv()


intents = discord.Intents().all()
client =  commands.Bot(command_prefix="-", intents=intents)
botUserId = str(os.getenv("BOTUSERID"))


serverId =  int(os.getenv("SERVERID"))
logChannelId = int(os.getenv("CHANNELID"))

@client.event
async def on_message(message):
    logChannel = discord.utils.get(message.guild.channels, id=logChannelId)
    if str(message.author.id) != botUserId: 
        await logChannel.send(f'{datetime.now().strftime("%d/%m/%y - %H:%M:%S")} IST\n**{message.author}**\n{message.content}')
    
    if not message.author.bot:
        with open("database/userStats.json", "r") as f:
            userStats = json.load(f)
        try:
            userStats[str(message.author.id)]["messageCount"] += 1
        except:
            if str(message.author.id) not in userStats:
                userStats[str(message.author.id)] = {"messageCount": 1, "warns": 0}
        
        with open("database/userStats.json", "w") as f:
            json.dump(userStats, f, indent=4)
    
    await client.process_commands(message)


@client.event
async def on_ready():
    print("Preparing")
    for files in os.listdir(os.path.join(os.getcwd(), "plugins")):
        if files.endswith(".py"):
            await client.load_extension(f"plugins.{files[:-3]}")
            print(f"{files[:-3]} has been loaded")
    print("Bot is online and ready to use")
    
    server = discord.utils.get(client.guilds, id=serverId)
    channel =  discord.utils.get(server.channels, id=logChannelId )
    await channel.send("The **Power Bot** is online \n This message is to inform that this channel has been set as logs channels \n all logs will be filed here")


@client.command()
async def load(ctx, extName):
    try:
        await client.load_extension(f"plugins.{extName}")
        await ctx.send(f"Extension {extName} loaded Successfully")
    except:
        await ctx.send("An error occured while performing the task")

@client.command()
async def reload(ctx):
    for files in os.listdir(".\plugins"):
        if files.endswith(".py"):
            try:
                await client.reload_extension(f"plugins.{files[:-3]}")
                await ctx.send(f"Extension {files} has been reloaded")
            except:
                await ctx.send(f"An error occured while reloading {files}")

@client.command()
async def unload(ctx, extName):
    try:
        await client.unload_extension(f"plugins.{extName}")
        await ctx.send(f"Extension {extName} has been unloaded")
    except:
        await client.send("An error occured while performing the task")
client.run(os.getenv("BOTTOKEN"))