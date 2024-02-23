import functools, os, asyncio

def no_blocking(func: callable):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        return await asyncio.to_thread(func, *args, **kwargs)
    return wrapper

@no_blocking
def start():
    server_dir = "G:/MinecraftServer"
    os.chdir(server_dir)
    serverInstance = os.system("start.bat")