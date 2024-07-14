import discord
from discord.ext import commands
from kodland_utils import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generate_password(ctx):
    await ctx.send(pass_gen(10))

@bot.command()
async def emoji(ctx):
    await ctx.send(random_emoji())

@bot.command()
async def number(ctx):
    await ctx.send(random_number())

@bot.command()
async def flipacoin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def helper(ctx):
    await ctx.send(helper1())

bot.run()
