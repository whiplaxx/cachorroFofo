import discord

from os import path as p
CURRENT_DIR = p.dirname(p.realpath(__file__))
from sys import path
path.append(CURRENT_DIR)

import low_functions

#alex = 277581722357465088
#kashmir = 298975463219396608
#biel = 247810079024349194

#🗿
#🖕

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

"""
- add reaction to message:
    emoji = "🤪"
    await message.add_reaction(emoji)

"""

client = MyClient()
client.run('Mzk4MDE0MDI5NTI1ODExMjAw.XqEj8g.fOb09RXhLzDhShL-ceINzghA0p8')
