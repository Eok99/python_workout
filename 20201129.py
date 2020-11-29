import discord
from discord.ext import commands
 
app = commands.Bot(command_prefix='/나')
 
@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)
     
     
app.run('NzgyNTkxODA4NzE3OTc5NjY5.X8Obaw.c1UG2WMjB1U80XSv7hYb2V19-eE
')