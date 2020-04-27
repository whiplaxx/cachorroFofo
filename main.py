import discord

from asyncio import sleep

from os import path as p
CURRENT_DIR = p.dirname(p.realpath(__file__))
from sys import path
path.append(CURRENT_DIR)

import low_functions
import functions

#🗿
#🖕

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        self.prefixo = '?'

    async def on_message(self, message):
        
        # don't respond to ourselves
        if message.author == self.user:
            return

        if low_functions.startsWith(message.content, self.prefixo):
            
            content = ( ( message.content )[1:len(message.content)] ).split(" ")
            await functions.handle(self, message, content)


"""
- add reaction to message:
    emoji = "🤪"
    await message.add_reaction(emoji)

"""

if __name__ == "__main__":
    tokenFile = open("botToken", 'r')
    token = tokenFile.read().replace('\n', '')
    tokenFile.close()

    client = MyClient()
    client.run(token)