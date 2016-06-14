import discord
import json
import random


with open('config.json') as file:
    config = json.load(file)

description = "Please ignore this bot"
client = discord.Client()
pot = 0


def placebet(points: int, outcome: str):
    global pot
    pot += points
    print(pot)


class PlaceBet():
    def __init__(self, points, outcome):
        self.points = points
        self.outcome = outcome


@client.event
async def on_ready():
    x = []
    for member in client.get_all_members():
        x.append(member.id)
    print(x)

    print('Connected')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bet'):
        try:
            command, points, outcome = message.content.split()
            if points.isdigit() and int(points) < 1000:
                msg = outcome + " " + points
                if outcome in ['win', 'lose']:
                    placebet(int(points), outcome)
                    msg = 'Bet placed for {}, the pot is now {}'.format(message.author.mention, pot)
                else:
                    msg = 'Please use the correct format\n!bet (AMOUNT) (OUTCOME)'
            else:
                msg = 'Please use the correct format\n!bet (AMOUNT) (OUTCOME)'
        except ValueError:
            return
            msg = 'Please use the correct format\n!bet (AMOUNT) (Win or Lose)'

        print(message.content)

        await client.send_message(message.channel, msg)

    if message.content.startswith('!help'):
        await client.send_message(message.channel, "Insert some help here\nYeezy just jumped over jumpman")

    if message.content.startswith('!okay'):
        await client.send_message(message.channel, 'okay okay okay okay okay OKAY https://streamable.com/om4j')

    if message.content.startswith('!fuckmeup'):
        msg = 'Hello {0.author.mention} https://www.youtube.com/watch?v=gbt61vcAkG0'.format(message)
        await client.send_message(message.channel, msg)


client.run(config['token'])