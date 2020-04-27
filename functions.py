import discord
import asyncio

from os import path as p
CURRENT_DIR = p.dirname(p.realpath(__file__))
from sys import path
path.append(CURRENT_DIR)

import low_functions

# BOT'S ID
client_id = 398014029525811200

# LIST ALL COMMANDS
async def sendHelp(f_client, message, content):

    help_msg = ""
    command_keys = commands.keys()

    for i in command_keys:
        help_msg += i + ": " + commands[i][1] + '\n'
    
    await message.channel.send( help_msg )

# SEND BOT'S INVITE LINK
async def invite(f_client, message, content):

    await message.channel.send("https://discordapp.com/oauth2/authorize?client_id=" + str(client_id) + "&scope=bot&permissions=8")

# WAIT N SECONDS
async def wait(f_client, message, content):
    
    time = int( content[1] )
    try:
        await asyncio.sleep( time )
    except:
        pass

    await message.channel.send("esperado " + str( time ) + " segundos")





# COMMANDS DIC
commands = {
    "ajuda": [sendHelp, "Lista todos os comandos"],

    "convite": [invite, "Link do convite do cachorro fofo"],
    
    "wait": [wait, "espera N segundos"]
}

# HANDLE MESSAGE CHATS WITH THE BOT PREFIX
async def handle(f_client, message, content):

    command = content[0]

    try:
        await commands[ command ][0]( f_client, message, content )
    except:
        await message.channel.send("?ajuda")