import discord
from discord.ext import commands
import random

description = "A little bot used for random things"
client = discord.Client()

@client.event
async def on_ready():
    print('Connected')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!help'):
        await client.send_message(message.channel, "! followed by a command\n!math Number Sign Number\n!roll Number\n!rolldnd NdN\n!choose this that\n!repeat Number Thing to repeat")

    if message.content.startswith('!join'):
        await client.join_voice_channel(client.get_channel(id='191602778446102529'))

    if message.content.startswith('!okay'):
        await client.send_message(message.channel, 'okay okay okay okay okay OKAY https://streamable.com/om4j')

    if message.content.startswith('!fuckmeup'):
        msg = 'Hello {0.author.mention} https://www.youtube.com/watch?v=gbt61vcAkG0'.format(message)
        await client.send_message(message.channel, msg)

# @bot.command()
# async def math(left : float, sign : str,right : float):
#     if sign == '+':
#         result = left + right
#     elif sign == '-':
#         result = left - right
#     elif sign == '/':
#         result = left / right
#     elif sign == '*':
#         result = left * right
#     await bot.say('The answer is ' + str(result))
#
# @bot.command()
# async def rolldnd(dice : str):
#     try:
#         rolls, limit = map(int, dice.split('d'))
#     except Exception:
#         await bot.say('Format has to be in NdN!')
#         return
#
#     result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#     await bot.say(result)
#
# @bot.command()
# async def roll(limit : int):
#     x = random.randint(1,limit)
#     await bot.say(x)
#
# @bot.command(description='For when you wanna settle the score some other way')
# async def choose(*choices : str):
#     await bot.say(random.choice(choices))
#
# @bot.command()
# async def repeat(times : int, content='repeating...'):
#     for i in range(times):
#         await bot.say(content)

client.run('MTkxNTMyMjU1NjMyNTU2MDMz.Cj7qDA.WDdgTHVv4kcnGDQVe7_dAJFGTWI')