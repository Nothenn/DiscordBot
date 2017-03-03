import discord, sys
import json

with open('config.json') as file:
    config = json.load(file)

with open('scoreboard.json') as readboard:
    scoreboard = json.load(readboard)

description = 'Please ignore this bot'
client = discord.Client()
players = {}
filename = "G:\DiscordBot\quinoa.png"


def placebet(points: int, outcome: str, idno: int):
    print(str(idno) + 'has placed a bet for ' + str(points))

    players[idno] = Player(idno)
    players[idno].setbet(points, outcome)


def betresult(outcome: str):
    for eyed in players:
        if players[eyed].outcome == outcome:
            givepoints(eyed, players[eyed].bet)
        else:
            takepoints(eyed, players[eyed].bet)

    with open('scoreboard.json', 'w') as f:
        json.dump(scoreboard, f, sort_keys=True, indent=4)


def givepoints(idno: int, points: int):
    scoreboard[idno] += points


def takepoints(idno: int, points:int):
    scoreboard[idno] -= points


def showpoints(idno: int):
    return scoreboard[idno]


class Player:
    def __init__(self, idno):
        self.idno = idno
        self.bet = 0
        self.outcome = None

    def setbet(self, bet, outcome):
        self.bet = bet
        self.outcome = outcome


@client.event
async def on_ready():
    global scoreboard
    global players

    print('Connected')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!result'):

        command, outcome = message.content.split()
        betresult(outcome)
        for idno in players:
            dude = message.author.server.get_member(players[idno].idno)
            msg = '{} has now got {} points'.format(dude.name, scoreboard[idno])
            await client.send_message(message.channel, msg)
        players.clear()

    if message.content.startswith('Points'):
        if message.author.id == '114777488458121218':
            givepoints(message.author.id, 10000)

    if message.content.startswith('!bet'):
        try:
            command, points, outcome = message.content.split()
            if points.isdigit():
                msg = outcome + ' ' + points
                if outcome in ['win', 'lose']:
                    try:
                        if players[message.author.id].outcome != outcome:
                            msg = '{} you have already bet the opposite'.format(message.author.mention)
                        else:
                            placebet(int(points), outcome, message.author.id)
                            msg = 'Bet placed for {}'.format(message.author.mention)
                    except KeyError:
                        placebet(int(points), outcome, message.author.id)
                        msg = 'Bet placed for {}'.format(message.author.mention)
                else:
                    msg = 'Please use the correct format\n!bet (AMOUNT) (OUTCOME)'
            elif players[message.author.id].points > points:
                msg = '{} You don\'t have that many points!'.format(message.author.mention)
            else:
                msg = 'Please use the correct format\n!bet (AMOUNT) (OUTCOME)'
        except ValueError:
            msg = 'Please use the correct format\n!bet (AMOUNT) (Win or Lose)'
            return
        await client.send_message(message.channel, msg)

    if message.content.startswith('!points'):
        msg = '{} has {} points'.format(message.author.mention, showpoints(message.author.id))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!quit'):
        await  client.send_message(message.channel, 'I am leaving now')
        sys.exit('Closing Down...')

    if message.content.startswith('!help'):
        await client.send_message(message.channel, 'Insert some help here')

    if message.content.startswith('!letsgo'):
        msg = 'Hello {0.author.mention} https://www.youtube.com/watch?v=gbt61vcAkG0'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!kanye'):
        await client.send_file(message.channel, filename)

    if message.content.startswith('!killme'):
        msg = '{} you are now dead'.format(message.author.mention)
        await client.send_message(message.channel, msg)

client.run(config['token'])
