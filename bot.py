import discord
import json
import random


with open('config.json') as file:
    config = json.load(file)

description = 'Please ignore this bot'
client = discord.Client()
pot = 0
x = {}
players = {}


def placebet(points: int, outcome: str, idno: int):
    print(str(idno) + 'has placed a bet for ' + str(points))

    global pot
    pot += points

    global players
    players[idno] = Player(idno)
    players[idno].setbet(points, outcome)


def betresult(outcome: str):
    print(outcome)
    for eyed in players:
        print(players[eyed].idno)
        print(players[eyed].outcome)
        if players[eyed].outcome == outcome:
            givepoints(eyed, pot)


def givepoints(idno: int, points: int):
    x[idno] += points


def potcommand(dothing):
    if dothing == 'empty':
        global pot
        pot = 0
    else:
        return pot


def showpoints(idno: int):
    return x[idno]


class Player:
    def __init__(self, idno):
        self.idno = idno
        self.points = 0
        self.outcome = None

    def setbet(self, points, outcome):
        self.points += points
        self.outcome = outcome
        print(self.outcome + ' IN PLAYER CLASS')


@client.event
async def on_ready():
    global x
    global players
    for member in client.get_all_members():
        x[member.id] = 0
    print(x)

    print('Connected')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!empty'):
        potcommand('empty')
        await client.send_message(message.channel, 'Pot Emptied')

    if message.content.startswith('!pot'):
        msg = 'The pot is currently {}'.format(potcommand('show'))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!result'):

        command, outcome = message.content.split()
        betresult(outcome)
        for idno in players:
            dude = message.author.server.get_member(players[idno].idno)
            msg = '{} has now got {} points'.format(dude.name, x[idno])
            await client.send_message(message.channel, msg)
            # players[idno].setbet(0, '')
        players.clear()
        potcommand('empty')

    if message.content.startswith('!bet'):
        try:
            command, points, outcome = message.content.split()
            if points.isdigit() and int(points) < 1000:
                msg = outcome + ' ' + points
                if outcome in ['win', 'lose']:
                    try:
                        if players[message.author.id].outcome != outcome:
                            msg = '{} you have already bet the opposite'.format(message.author.mention)
                        else:
                            placebet(int(points), outcome, message.author.id)
                            msg = 'Bet placed for {}, the pot is now {}'.format(message.author.mention, pot)
                    except KeyError:
                        placebet(int(points), outcome, message.author.id)
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

    if message.content.startswith('!points'):
        msg = '{} has {} points'.format(message.author.mention, showpoints(message.author.id))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!help'):
        await client.send_message(message.channel, 'Insert some help here\nYeezy just jumped over jumpman')

    if message.content.startswith('!okay'):
        await client.send_message(message.channel, 'okay okay okay okay okay OKAY https://streamable.com/om4j')

    if message.content.startswith('!fuckmeup'):
        msg = 'Hello {0.author.mention} https://www.youtube.com/watch?v=gbt61vcAkG0'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('kill me'):
        msg = '{} you are now dead'.format(message.author.mention)
        await client.send_message(message.channel, msg)

client.run(config['token'])