import discord
from discord.ext import commands
import random

description = "A little bot used for random things"
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description=description)

@bot.event
async def on_ready():
    print('Connected')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('BotHelp'):
        msg = "Either {} or ! followed by the command\n!math Number Sign Number\n!roll Number\n!rolldnd NdN\n!choose this that\n!repeat Number Thing to repeat".format(bot.user.mention)
        await bot.send_message(message.channel, msg)

    if message.content.startswith('!FuckMeUpFam'):
        msg = '!FuckMeUpFam'
        # msg = 'Hello {0.author.mention} https://www.youtube.com/watch?v=gbt61vcAkG0'.format(message)
        await bot.send_message(message.channel, msg)


@bot.command()
async def math(left : float, sign : str,right : float):
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