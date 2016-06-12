import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='#', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def hey(message):
    # we do not want the bot to reply to itself
    if message.content.startswith('#hey'):
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)
    if message.content.startswith('http'):
        msg = '{0.author.mention} mate stop with the links'.format(message)
        await bot.send_message(message.channel, msg)

@bot.command()
async def math(left : float, sign : str,right : float):
    result = 0
    
    if sign == '+':
        result = left + right
    elif sign == '-':
        result = left - right
    elif sign == '/':
        result = left / right
    elif sign == '*':
        result = left * right
    await bot.say('The answer is ' + str(result))

@bot.command()
async def rolldnd(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command()
async def roll(limit : int):
    x = random.randint(1,limit)
    await bot.say(x)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    for i in range(times):
        await bot.say(content)

bot.run('MTkxNTMyMjU1NjMyNTU2MDMz.Cj7qDA.WDdgTHVv4kcnGDQVe7_dAJFGTWI')