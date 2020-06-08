import discord
from discord.ext import commands

token = ''

with open('config.txt', 'r') as file:
    token = file.readline().strip()

bot = commands.Bot(command_prefix='*', case_insensitive=True)


@bot.event
async def on_ready():
    print('bot online')


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # await message.channel.send('Pong')
    await bot.process_commands(message)

@bot.command(name='test')
async def test(ctx):
    await ctx.send('test recieved')

@bot.command(name='img')
async def img(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/719630067260719138/719639583117017149/o0htmc6mzk351.png')

bot.run(token)

