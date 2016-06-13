import discord
import json
import random


def math(left: float, sign: str, right: float):
    if sign == '+':
        result = left + right
    elif sign == '-':
        result = left - right
    elif sign == '/':
        result = left / right
    elif sign == '*':
        result = left * right
    return 'The answer is ' + str(result)


def dndroll(dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        return 'Format has to be in NdN!'

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    return result


def roll(limit : int):
    x = random.randint(1,limit)
    return x


with open('config.json') as file:
    config = json.load(file)

description = "Please ignore this bot"
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
        await client.send_message(message.channel, "Insert some help here\nYeezy just jumped over jumpman")

    if message.content.startswith('!join'):
        await client.join_voice_channel(client.get_channel(id='191602778446102529'))

    if message.content.startswith('!okay'):
        await client.send_message(message.channel, 'okay okay okay okay okay OKAY https://streamable.com/om4j')

    if message.content.startswith('!fuckmeup'):
        msg = 'Hello {0.author.mention} https://www.youtube.com/watch?v=gbt61vcAkG0'.format(message)
        await client.send_message(message.channel, msg)


client.run(config['token'])