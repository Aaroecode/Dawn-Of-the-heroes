from discord.ext import commands
import discord, dotenv, os
intents = discord.Intents.all()
dotenv.load_dotenv()
client  =  commands.Bot(command_prefix=".", intents=intents)

@client.event
async def on_ready():
    print("Bot is ready to server")
    path = os.path.join(os.getcwd(), "plugins")
    for files in os.listdir(path):
        if files.endswith(".py"):
            await client.load_extension(f'plugins.{files[:-3]}')
            print(f"Extension {files} has been loaded")
    
botToken = os.getenv("BOT_TOKEN")
client.run(botToken)