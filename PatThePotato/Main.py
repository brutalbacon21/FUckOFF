'''
Pat The Discord Bot:

First time using the script?
Please insure that the Dependencies.py has been ran before
trying to run the script

Supported versions:
Python 3.8 or newer
'''

import discord
import random
import time
import threading
from discord.ext import commands
import youtube_dl  # not being used yet

# Variables
client = commands.Bot(command_prefix='~')
client.remove_command('help')
ydl_opts = {}  # Not in use yet
Token = 'NzQ0NDE4NTcyOTc3MTc2NjU3.Xzi70g.dEsO_zezbieOase59MwS9j3jadI'


# Console Events
@client.event
async def on_ready():
    print('Bot is Active')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


# Bot Commands
@client.command()
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency * 1000)}ms')  # Ping's the bot for it's latency but
    # client.latency is using seconds so it needs to be multiplied by 1000 to get it to ms


@client.command(aliases=['8ball', 'eightball'])  # The brackets are for setting aliases so u can use multiple
# commands for one function
async def _8ball(ctx, *, question):  # ctx, etc.. are passing commands into the async function to be used. *
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Dont count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.', ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')  # random.choice pick a random
    # value out of a list


@client.command(aliases=['purge'])
async def clear(ctx, amount=5):  # ctx is the command ~clear and amount is the number after such as 5 which it defaults
    await ctx.channel.purge(limit=amount)  # Purge is a method in discord

@client.command()
async def mission(ctx):
    mtime = 30
    genre = [
        'Future Bass',
        'IDM - (intelligent dance music)',
        'Trance',
        'Dubstep',
        'Drum And Bass',
        'Trap',
        'LoFi',
        'Ambient',
    ]
    modifier = [
        'Use the Resonator in a weird way',
        'Use some form of Granular Synthesis',
        'Own samples only',
        'No modifier this round',
        'Use a Vocoder in a weird way',
        'Must Contain Guitar',
        'Must Contain a 7th'

    ]
    key = [
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'A#',
        'B#',
        'C#',
        'D#',
        'E#',
        'F#',
        'G#',
    ]
    mood = [
        'Major',
        'Minor'
    ]
    await ctx.send(f'''
Objective:
Make a 4 bar loop with the information below

Genre
---------
{random.choice(genre)}

Key
---------
{random.choice(key), random.choice(mood)}

Modifier
---------
{random.choice(modifier)}
    ''')
    while mtime != 0:
        print(' ')
        await ctx.send(f'You have {mtime} Minutes remaining!!')
        threading.Thread(time.sleep(300))
        mtime = mtime - 5
    await ctx.send('TIMES UP!!')


# Run
client.run(Token)
